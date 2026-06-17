import torch
import os
from gpt1 import GPT1LanguageModel

# Hyperparameters (must match the trained books model)
block_size = 512     # Context window set to 512 characters!
n_embd = 128
n_head = 4
n_layer = 4
dropout = 0.0
device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'

# Load vocabulary
data_path = "data/input_books.txt"
if not os.path.exists(data_path):
    print("Error: data/input_books.txt not found. Run generate_books_data.py first.")
    exit(1)

with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s if c in stoi]
decode = lambda l: ''.join([itos[i] for i in l])

# Initialize model
model = GPT1LanguageModel(
    vocab_size=vocab_size,
    n_embd=n_embd,
    n_head=n_head,
    n_layer=n_layer,
    block_size=block_size,
    dropout=dropout,
    device=device
).to(device)

# Load trained weights
weights_path = 'weights/gpt1_books.pth'
if os.path.exists(weights_path):
    model.load_state_dict(torch.load(weights_path, map_location=device))
else:
    print(f"Error: {weights_path} not found.")
    exit(1)

model.eval()

# Prompt loop
print("\n" + "="*70)
print("GPT-1 Reasoning Book Passage Generator (Context Window: 512)")
print("="*70)
print("Enter a book title or starting words (e.g. 'Book: Sapiens: The Cognitive', 'Book: Sherlock')")
user_prompt = input("Your Prompt: ").strip()

context = torch.tensor([encode(user_prompt)], dtype=torch.long, device=device)

print("\n--- Model Response ---")
generated_seq = model.generate(context, max_new_tokens=400)[0].tolist()
print(decode(generated_seq))
