import torch
import os
from gpt1 import GPT1LanguageModel

# ─── Hyperparameters ──────────────────────────────────────
batch_size    = 64
block_size    = 256
max_iters     = 10000
eval_interval = 500
learning_rate = 3e-4
device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'
eval_iters    = 50
n_embd        = 192       # slightly bigger embedding for richer vocabulary
n_head        = 6
n_layer       = 6
dropout       = 0.2       # prevents memorisation, encourages generalisation
# ─────────────────────────────────────────────────────────

print(f"Using device: {device}")

# 1. Read dataset
data_path = "data/input_basic.txt"
if not os.path.exists(data_path):
    print("Error: data/input_basic.txt not found. Run generate_basic_data.py first.")
    exit(1)

with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Dataset loaded: {len(text):,} characters")

# 2. Tokenizer
chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s if c in stoi]
decode = lambda l: ''.join([itos[i] for i in l])

# 3. Train / val split
data = torch.tensor(encode(text), dtype=torch.long)
n = int(0.9 * len(data))
train_data = data[:n]
val_data   = data[n:]

print(f"Vocab size: {vocab_size} | Train tokens: {len(train_data):,} | Val tokens: {len(val_data):,}")

def get_batch(split):
    d = train_data if split == 'train' else val_data
    ix = torch.randint(len(d) - block_size, (batch_size,))
    x = torch.stack([d[i:i+block_size] for i in ix])
    y = torch.stack([d[i+1:i+block_size+1] for i in ix])
    return x.to(device), y.to(device)

@torch.no_grad()
def estimate_loss(model):
    out = {}
    model.eval()
    for split in ['train', 'val']:
        losses = torch.zeros(eval_iters)
        for k in range(eval_iters):
            X, Y = get_batch(split)
            _, loss = model(X, Y)
            losses[k] = loss.item()
        out[split] = losses.mean()
    model.train()
    return out

# 4. Model
model = GPT1LanguageModel(
    vocab_size=vocab_size,
    n_embd=n_embd,
    n_head=n_head,
    n_layer=n_layer,
    block_size=block_size,
    dropout=dropout,
    device=device
).to(device)

weights_path = 'weights/gpt1_basic.pth'
if os.path.exists(weights_path):
    print(f"Resuming from {weights_path}...")
    try:
        checkpoint = torch.load(weights_path, map_location=device)
        ckpt_vocab = checkpoint['token_embedding_table.weight'].shape[0]
        if ckpt_vocab != vocab_size:
            print(f"Vocab mismatch ({ckpt_vocab} vs {vocab_size}). Adapting...")
            md = model.state_dict()
            mv = min(ckpt_vocab, vocab_size)
            md['token_embedding_table.weight'][:mv] = checkpoint['token_embedding_table.weight'][:mv]
            md['lm_head.weight'][:mv]               = checkpoint['lm_head.weight'][:mv]
            md['lm_head.bias'][:mv]                 = checkpoint['lm_head.bias'][:mv]
            for k, v in checkpoint.items():
                if k not in ['token_embedding_table.weight', 'lm_head.weight', 'lm_head.bias']:
                    md[k] = v
            model.load_state_dict(md)
        else:
            model.load_state_dict(checkpoint)
        print("Weights loaded successfully.")
    except Exception as e:
        print(f"Could not load weights: {e}. Starting fresh.")

num_params = sum(p.numel() for p in model.parameters()) / 1e6
print(f"Parameters: {num_params:.2f}M | Block size: {block_size} | Dropout: {dropout}")

optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

# 5. Training loop
best_val_loss = float('inf')
print("\n--- Starting Basic Knowledge Training ---")

for it in range(max_iters):
    if it % eval_interval == 0 or it == max_iters - 1:
        losses = estimate_loss(model)
        tag = ""
        if losses['val'] < best_val_loss:
            best_val_loss = losses['val']
            torch.save(model.state_dict(), weights_path)
            tag = " <-- saved best"
        print(f"step {it:>5}: train loss {losses['train']:.4f} | val loss {losses['val']:.4f}{tag}")

    xb, yb = get_batch('train')
    _, loss = model(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()

# Final save
torch.save(model.state_dict(), weights_path)
print(f"\nTraining complete. Weights saved to {weights_path}")

# 6. Quick generation test
print("\n--- Sample Outputs ---")
test_prompts = [
    "Instruction: hello\nResponse:",
    "Instruction: what is the meaning of happy\nResponse:",
    "Instruction: what is 5 plus 3\nResponse:",
    "Instruction: what color is the sky\nResponse:",
    "Instruction: how many days are in a week\nResponse:",
    "Instruction: what is a dog\nResponse:",
]
model.eval()
for prompt in test_prompts:
    ctx = torch.tensor([encode(prompt)], dtype=torch.long, device=device)
    out = decode(model.generate(ctx, max_new_tokens=80)[0].tolist())
    response = out.split("Response:")[-1].strip().split("Instruction:")[0].strip()
    print(f"  Q: {prompt.split('Instruction:')[1].split(chr(10))[0].strip()}")
    print(f"  A: {response}")
    print()
