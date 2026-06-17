import torch
import os
import sys
from gpt1 import GPT1LanguageModel

# Unified Architecture config
block_size = 128
n_embd = 128
n_head = 4
n_layer = 4
dropout = 0.0
device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'

# Model Vocab loading from input_master.txt
dataset_path = "input_master.txt"
weights_path = "gpt1_master.pth"

if not os.path.exists(dataset_path) or not os.path.exists(weights_path):
    print("Error: Missing master dataset or model weights. Train the model first.")
    exit(1)

with open(dataset_path, 'r', encoding='utf-8') as f:
    text = f.read()

chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s if c in stoi]
decode = lambda l: ''.join([itos[i] for i in l])

# Initialize the single master model
model = GPT1LanguageModel(
    vocab_size=vocab_size,
    n_embd=n_embd,
    n_head=n_head,
    n_layer=n_layer,
    block_size=block_size,
    dropout=dropout,
    device=device
).to(device)

model.load_state_dict(torch.load(weights_path, map_location=device))
model.eval()

# Supported dictionary words for routing
dict_words = ["aberration", "benevolent", "cacophony", "diligent", "ephemeral", 
              "fortuitous", "gregarious", "harangue", "inevitable", "juxtaposition", 
              "laconical", "mitigate", "nefarious", "ostentatious", "pragmatic", 
              "querulous", "resilient", "scrutinize", "taciturn", "ubiquitous", 
              "venerable", "wary", "zealous"]

def detect_mode(prompt):
    p_lower = prompt.strip().lower()
    
    # 1. IDS Network Log
    if "proto=" in p_lower or "spt=" in p_lower or "dpt=" in p_lower or "dst=" in p_lower:
        return "ids"
        
    # 2. Dictionary Lookup
    if p_lower in dict_words:
        return "dictionary"
        
    # 3. Shakespeare Dialog
    if (prompt.isupper() and prompt.endswith(":")) or p_lower.startswith("romeo") or p_lower.startswith("hamlet") or p_lower.startswith("juliet"):
        return "shakespeare"
        
    # 4. Default to Student Study Helper
    return "student"

def answer_prompt(user_prompt):
    mode = detect_mode(user_prompt)
    
    # Format prompt input depending on the identified mode
    if mode == "ids" or mode == "shakespeare":
        formatted_prompt = user_prompt
    elif mode == "dictionary":
        formatted_prompt = f"Word: {user_prompt.lower()}\n"
    else:
        formatted_prompt = f"Question: {user_prompt.lower()}\nAnswer:"

    context = torch.tensor([encode(formatted_prompt)], dtype=torch.long, device=device)
    generated = model.generate(context, max_new_tokens=150)[0].tolist()
    full_response = decode(generated)

    # Clean the formatted output block
    if mode == "student":
        try:
            return f"[STUDENT TUTOR MODE]\n{full_response.split('Answer:')[1].split('Question:')[0].strip()}"
        except IndexError:
            return f"[STUDENT TUTOR MODE]\n{full_response.strip()}"
    elif mode == "dictionary":
        try:
            return f"[DICTIONARY LOOKUP MODE]\nWord: {full_response.split('Word:')[1].split('Word:')[0].strip()}"
        except IndexError:
            return f"[DICTIONARY LOOKUP MODE]\n{full_response.strip()}"
    else:
        return f"[{mode.upper()} MODE]\n{full_response.strip()}"

def main():
    print("\n" + "="*60)
    print("      GPT-1 MASTER UNIFIED ASSISTANT (Loaded: 1 Model)")
    print("="*60)
    print("Ask questions, enter dictionary words, Shakespeare names, or network queries.")
    print("Type 'exit' to quit.")
    print("="*60)
    
    while True:
        try:
            user_prompt = input("\nYour Prompt: ").strip()
            if not user_prompt:
                continue
            if user_prompt.lower() == 'exit':
                print("Goodbye!")
                break
                
            response = answer_prompt(user_prompt)
            print(f"\n{response}")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
