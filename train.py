import torch
import urllib.request
import os
import ssl
from gpt1 import GPT1LanguageModel

# Bypass SSL verification for certificate issue on macOS
ssl._create_default_https_context = ssl._create_unverified_context


# Hyperparameters
batch_size = 32      # how many independent sequences will we process in parallel?
block_size = 128     # what is the maximum context length for predictions?
max_iters = 26000
eval_interval = 2600
learning_rate = 3e-4 # lower learning rate for fine-tuning
device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'
eval_iters = 50
n_embd = 128
n_head = 4
n_layer = 4
dropout = 0.1


print(f"Using device: {device}")

# 1. Download and read dataset
data_url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/data/input.txt"
data_path = "data/input.txt"
if not os.path.exists(data_path):
    print("Downloading Tiny Shakespeare dataset...")
    urllib.request.urlretrieve(data_url, data_path)

with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 2. Set up character-level tokenizer
chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s] # encoder: take a string, output a list of integers
decode = lambda l: ''.join([itos[i] for i in l]) # decoder: take a list of integers, output a string

# 3. Train and test splits
data = torch.tensor(encode(text), dtype=torch.long)
n = int(0.9 * len(data)) # first 90% will be train, rest val
train_data = data[:n]
val_data = data[n:]

# 4. Data loading helper
def get_batch(split):
    # generate a small batch of data of inputs x and targets y
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

# 5. Model Initialization
model = GPT1LanguageModel(
    vocab_size=vocab_size,
    n_embd=n_embd,
    n_head=n_head,
    n_layer=n_layer,
    block_size=block_size,
    dropout=dropout,
    device=device
).to(device)

# Load existing weights if they exist to resume training
weights_path = 'weights/gpt1_shakespeare.pth'
if os.path.exists(weights_path):
    print(f"Loading existing model weights from {weights_path} to resume training...")
    model.load_state_dict(torch.load(weights_path, map_location=device))

# Print parameter count
num_params = sum(p.numel() for p in model.parameters()) / 1e6
print(f"{num_params:.2f}M parameters")


# Create a PyTorch optimizer
optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

# 6. Training Loop
for iter in range(max_iters):
    # evaluate the loss on train and val sets every eval_interval
    if iter % eval_interval == 0 or iter == max_iters - 1:
        losses = estimate_loss(model)
        print(f"step {iter}: train loss {losses['train']:.4f}, val loss {losses['val']:.4f}")

    # sample a batch of data
    xb, yb = get_batch('train')

    # evaluate the loss
    logits, loss = model(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()

# Save the trained model weights
torch.save(model.state_dict(), 'weights/gpt1_shakespeare.pth')
print("Model weights saved to weights/gpt1_shakespeare.pth")

# 7. Generate some text from the model
print("\n--- Generating sample text ---")
context = torch.zeros((1, 1), dtype=torch.long, device=device) # starting with newline character token
generated_seq = model.generate(context, max_new_tokens=500)[0].tolist()
print(decode(generated_seq))
