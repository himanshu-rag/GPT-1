import torch
import os
from gpt1 import GPT1LanguageModel

# Hyperparameters (must match the trained instruction model)
block_size = 128
n_embd = 128
n_head = 4
n_layer = 4
dropout = 0.0
device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'

# Load vocabulary
data_path = "input_instructions.txt"
if not os.path.exists(data_path):
    print("Error: input_instructions.txt not found. Run generate_instruction_data.py first.")
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
weights_path = 'gpt1_instructions.pth'
if os.path.exists(weights_path):
    model.load_state_dict(torch.load(weights_path, map_location=device))
else:
    print(f"Error: {weights_path} not found.")
    exit(1)

model.eval()

# Prompt loop
print("\n" + "="*70)
print("GPT-1 Instruction & FAQ Generator")
print("="*70)
print("Enter an instruction (e.g. 'translate 'thank you' to spanish', 'how do i reset my router')")
user_prompt = input("Your Prompt: ").strip().lower()

prompt = f"Instruction: {user_prompt}\nResponse:"
context = torch.tensor([encode(prompt)], dtype=torch.long, device=device)

print("\n--- Model Response ---")
generated_seq = model.generate(context, max_new_tokens=200)[0].tolist()
# Get only the generated response part
full_response = decode(generated_seq)
response_part = full_response.split("Response:")[1].split("Instruction:")[0].strip()
print(response_part)
