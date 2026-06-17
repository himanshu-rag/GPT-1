import torch
import os
from gpt1 import GPT1LanguageModel

# Hyperparameters (must match the trained English model)
block_size = 128
n_embd = 128
n_head = 4
n_layer = 4
dropout = 0.0
device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'

# Load vocabulary
data_path = "data/input_english.txt"
if not os.path.exists(data_path):
    print("Error: data/input_english.txt not found. Run generate_english_data.py first.")
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
weights_path = 'weights/gpt1_english.pth'
if os.path.exists(weights_path):
    model.load_state_dict(torch.load(weights_path, map_location=device))
else:
    print(f"Error: {weights_path} not found.")
    exit(1)

model.eval()

# Prompt loop
print("\n" + "="*50)
print("GPT-1 English & Network Chatbot")
print("="*50)
print("Ask me anything! (e.g. 'hello', 'what is your name', 'tell me a joke', 'what is tcp')")
user_question = input("Your Question: ").strip().lower()

prompt = f"Question: {user_question}\nAnswer:"
context = torch.tensor([encode(prompt)], dtype=torch.long, device=device)

print("\n--- Model Response ---")
generated_seq = model.generate(context, max_new_tokens=250)[0].tolist()
# Get only the generated answer part
full_response = decode(generated_seq)
answer_part = full_response.split("Answer:")[1].split("Question:")[0].strip()
print(answer_part)
