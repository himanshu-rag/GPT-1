import torch
import urllib.request
import os
import ssl
from gpt1 import GPT1LanguageModel

# Bypass SSL verification for macOS
ssl._create_default_https_context = ssl._create_unverified_context

# Hyperparameters
batch_size = 32
block_size = 256     # 256-character context window for learning complete paragraphs
max_iters = 8000     # 8000 iterations to learn the full book structure
eval_interval = 1000
learning_rate = 5e-4 # lower learning rate for stable convergence on a whole book
device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'
eval_iters = 50
n_embd = 128
n_head = 4
n_layer = 4
dropout = 0.1

print(f"Using device: {device}")

# 1. Download and Clean "Alice's Adventures in Wonderland"
book_url = "https://www.gutenberg.org/files/11/11-0.txt"
raw_path = "alice_raw.txt"
clean_path = "alice.txt"

if not os.path.exists(clean_path):
    print("Downloading 'Alice's Adventures in Wonderland' from Project Gutenberg...")
    urllib.request.urlretrieve(book_url, raw_path)
    
    # Clean Project Gutenberg headers/footers
    with open(raw_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Look for standard Gutenberg book start/end markers
    start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK ALICE'S ADVENTURES IN WONDERLAND ***"
    end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK ALICE'S ADVENTURES IN WONDERLAND ***"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        # Extract only the book content
        book_content = content[start_idx + len(start_marker):end_idx].strip()
    else:
        book_content = content.strip() # fallback if markers change
        
    with open(clean_path, 'w', encoding='utf-8') as f:
        f.write(book_content)
    print("Book text cleaned and saved to alice.txt")

# Load dataset
with open(clean_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 2. Tokenizer
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
print(f"Model vocab size: {vocab_size} | Parameter count: {num_params:.2f}M | Context Window: {block_size}")

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
torch.save(model.state_dict(), 'gpt1_alice.pth')
print("Model weights saved to gpt1_alice.pth")

# 6. Generate sample text
print("\n--- Generating sample text from the book ---")
context = torch.tensor([encode("CHAPTER I.\nDown the Rabbit-Hole\n\nAlice was beginning to get very tired")], dtype=torch.long, device=device)
generated_seq = model.generate(context, max_new_tokens=400)[0].tolist()
print(decode(generated_seq))
