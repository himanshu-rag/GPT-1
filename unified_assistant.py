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

# Load Dictionary words for routing
dict_words = ["aberration", "benevolent", "cacophony", "diligent", "ephemeral", 
              "fortuitous", "gregarious", "harangue", "inevitable", "juxtaposition", 
              "laconical", "mitigate", "nefarious", "ostentatious", "pragmatic", 
              "querulous", "resilient", "scrutinize", "taciturn", "ubiquitous", 
              "venerable", "wary", "zealous"]

def detect_model_mode(prompt):
    p_lower = prompt.strip().lower()
    
    # 1. Check if it's an IDS Network Log format
    if "proto=" in p_lower or "spt=" in p_lower or "dpt=" in p_lower or "dst=" in p_lower:
        return "ids"
        
    # 2. Check if it is a dictionary word lookup
    if p_lower in dict_words:
        return "dictionary"
        
    # 3. Check if it's a Shakespeare character dialog prompt (e.g. 'ROMEO:', uppercase ending with colon)
    if (prompt.isupper() and prompt.endswith(":")) or p_lower.startswith("romeo") or p_lower.startswith("hamlet") or p_lower.startswith("juliet"):
        return "shakespeare"
        
    # 4. Default to 10th-grade study companion for general English questions
    return "student"

def run_inference(mode, user_prompt):
    # Determine files based on mode
    if mode == "ids":
        dataset = "input_ids.txt"
        weights = "gpt1_ids.pth"
        formatted_prompt = user_prompt
    elif mode == "dictionary":
        dataset = "input_dictionary.txt"
        weights = "gpt1_dictionary.pth"
        formatted_prompt = f"Word: {user_prompt.lower()}\n"
    elif mode == "shakespeare":
        dataset = "input.txt"
        weights = "gpt1_shakespeare.pth"
        formatted_prompt = user_prompt
    else: # student
        dataset = "input_student.txt"
        weights = "gpt1_student.pth"
        formatted_prompt = f"Question: {user_prompt.lower()}\nAnswer:"

    # Load dataset to extract vocab
    with open(dataset, 'r', encoding='utf-8') as f:
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
    
    model.load_state_dict(torch.load(weights, map_location=device))
    model.eval()

    context = torch.tensor([encode(formatted_prompt)], dtype=torch.long, device=device)
    generated = model.generate(context, max_new_tokens=150)[0].tolist()
    full_response = decode(generated)

    # Post-process response output
    if mode == "student":
        return full_response.split("Answer:")[1].split("Question:")[0].strip()
    elif mode == "dictionary":
        return full_response.split("Word:")[1].split("Word:")[0].strip()
    else:
        return full_response.strip()

def main():
    if len(sys.argv) < 2:
        # If run interactively
        print("\n" + "="*50)
        print("          SMART GPT-1 UNIFIED ASSISTANT")
        print("="*50)
        user_prompt = input("Enter your prompt: ").strip()
    else:
        user_prompt = " ".join(sys.argv[1:]).strip()

    if not user_prompt:
        print("Error: Empty prompt received.")
        return

    mode = detect_model_mode(user_prompt)
    
    try:
        response = run_inference(mode, user_prompt)
        print(f"\n[Identified Model Mode: {mode.upper()}]")
        print(f"Response:\n{response}")
    except Exception as e:
        print(f"\nError running model {mode}: {e}")

if __name__ == "__main__":
    main()
