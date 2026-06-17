import torch
import os
from gpt1 import GPT1LanguageModel

# Hyperparameters (must match the trained model)
block_size = 128
n_embd = 128
n_head = 4
n_layer = 4
dropout = 0.0
device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'

# Load vocabulary and token mapping from training dataset
data_path = "data/input.txt"
if not os.path.exists(data_path):
    print("Error: data/input.txt not found. Run train.py first to download the dataset.")
    exit(1)

with open(data_path, 'r', encoding='utf-8') as f:
    text = f.read()

chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s]
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
weights_path = 'weights/gpt1_shakespeare.pth'
if os.path.exists(weights_path):
    model.load_state_dict(torch.load(weights_path, map_location=device))
    print(f"Loaded model weights from {weights_path}")
else:
    print(f"Error: {weights_path} not found. Train the model first.")
    exit(1)

model.eval()

# Let user prompt the model
print("\n" + "="*50)
print("GPT-1 Text Generator")
print("="*50)
prompt = input("Enter a starting prompt (or press Enter for a newline): ")
if not prompt:
    prompt = "\n"

# Encode prompt and generate
context = torch.tensor([encode(prompt)], dtype=torch.long, device=device)
print("\n--- Generating response ---")
generated_seq = model.generate(context, max_new_tokens=500)[0].tolist()
print(decode(generated_seq))
