import torch
import urllib.request
import os
import ssl
from gpt1 import GPT1LanguageModel

# Bypass SSL verification for macOS issues
ssl._create_default_https_context = ssl._create_unverified_context

# Hyperparameters
batch_size = 32
block_size = 128
max_iters = 5000      # 5000 steps is good to get clear networking concepts
eval_interval = 500
learning_rate = 1e-3
device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'
eval_iters = 50
n_embd = 128
n_head = 4
n_layer = 4
dropout = 0.1

print(f"Using device: {device}")

# 1. Download and compile Networking RFCs
rfc_urls = {
    "RFC 793 (TCP)": "https://www.ietf.org/rfc/rfc793.txt",
    "RFC 791 (IP)": "https://www.ietf.org/rfc/rfc791.txt",
    "RFC 768 (UDP)": "https://www.ietf.org/rfc/rfc768.txt"
}
data_path = "input_networking.txt"

if not os.path.exists(data_path):
    print("Compiling networking dataset from IETF RFC specifications...")
    compiled_text = ""
    for name, url in rfc_urls.items():
        print(f"Downloading {name}...")
        try:
            with urllib.request.urlopen(url) as response:
                compiled_text += response.read().decode('utf-8', errors='ignore') + "\n\n"
        except Exception as e:
            print(f"Failed to download {name}: {e}")
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(compiled_text)
    print("Dataset saved to input_networking.txt")

with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 2. Tokenizer setup
chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s if c in stoi]
decode = lambda l: ''.join([itos[i] for i in l])

# 3. Train/val split
data = torch.tensor(encode(text), dtype=torch.long)
n = int(0.9 * len(data))
train_data = data[:n]
val_data = data[n:]

def get_batch(split):
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    x, y = x.to(device), y.to(device)
    return x, y

@torch.no_grad()
def estimate_loss(model):
    out = {}
    model.eval()
    for split in ['train', 'val']:
        losses = torch.zeros(eval_iters)
        for k in range(eval_iters):
            X, Y = get_batch(split)
            logits, loss = model(X, Y)
            losses[k] = loss.item()
        out[split] = losses.mean()
    model.train()
    return out

# 4. Model Initialization
model = GPT1LanguageModel(
    vocab_size=vocab_size,
    n_embd=n_embd,
    n_head=n_head,
    n_layer=n_layer,
    block_size=block_size,
    dropout=dropout,
    device=device
).to(device)

num_params = sum(p.numel() for p in model.parameters()) / 1e6
print(f"Model vocab size: {vocab_size} | Parameter count: {num_params:.2f}M")

optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

# 5. Training Loop
for iter in range(max_iters):
    if iter % eval_interval == 0 or iter == max_iters - 1:
        losses = estimate_loss(model)
        print(f"step {iter}: train loss {losses['train']:.4f}, val loss {losses['val']:.4f}")

    xb, yb = get_batch('train')
    logits, loss = model(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()

# Save the trained model weights
torch.save(model.state_dict(), 'gpt1_networking.pth')
print("Model weights saved to gpt1_networking.pth")

# 6. Generate sample text
print("\n--- Generating sample networking text ---")
context = torch.zeros((1, 1), dtype=torch.long, device=device) # space/newline
generated_seq = model.generate(context, max_new_tokens=500)[0].tolist()
print(decode(generated_seq))
