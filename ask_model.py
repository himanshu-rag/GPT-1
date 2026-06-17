import torch
import os
from gpt1 import GPT1LanguageModel

# Hyperparameters (must match the trained IDS model)
block_size = 128
n_embd = 128
n_head = 4
n_layer = 4
dropout = 0.0
device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'

# Load vocabulary
with open("input_ids.txt", 'r', encoding='utf-8') as f:
    text = f.read()

chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s if c in stoi]
decode = lambda l: ''.join([itos[i] for i in l])

# Initialize model and load weights
model = GPT1LanguageModel(
    vocab_size=vocab_size,
    n_embd=n_embd,
    n_head=n_head,
    n_layer=n_layer,
    block_size=block_size,
    dropout=dropout,
    device=device
).to(device)

model.load_state_dict(torch.load('gpt1_ids.pth', map_location=device))
model.eval()

def ask_scenario(prompt, scenario_desc):
    print("\n" + "="*70)
    print(f"QUERY SCENARIO: {scenario_desc}")
    print(f"PROMPT SENT: '{prompt}'")
    print("="*70)
    
    context = torch.tensor([encode(prompt)], dtype=torch.long, device=device)
    generated = model.generate(context, max_new_tokens=100)[0].tolist()
    # Decode up to the first newline or end of segment
    full_output = decode(generated)
    first_log_line = full_output.split('\n')[0]
    print(f"MODEL RESPONSE: {first_log_line}")

# Run queries
ask_scenario(
    "proto=TCP src=198.51.100.12",
    "Identifying Attacker Behavior (Brute Force / Web Attack)"
)

ask_scenario(
    "proto=TCP src=192.168.1.112",
    "Botnet Beacon Detection"
)

ask_scenario(
    "proto=TCP src=198.51.100.55 spt=43291 dst=192.168.1.20 dpt=80 payload=\"GET /index.php?id=",
    "Reconstructing Web SQL Injection Signature"
)
