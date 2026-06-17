import torch
import os
import sys
from gpt1 import GPT1LanguageModel

# Unified Architecture config (all models are matching size)
block_size = 128
n_embd = 128
n_head = 4
n_layer = 4
dropout = 0.0
device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'

# Model Modes metadata
MODES = {
    "1": {
        "name": "Shakespeare Dialog Generator",
        "weights": "gpt1_shakespeare.pth",
        "dataset": "input.txt",
        "prompt_hint": "Enter character name or dialog start (e.g. 'ROMEO:', 'HAMLET:')"
    },
    "2": {
        "name": "Network Intrusion Detection (IDS) Log Generator",
        "weights": "gpt1_ids.pth",
        "dataset": "input_ids.txt",
        "prompt_hint": "Enter log filter prefix (e.g. 'proto=TCP src=198.51.100.12', 'proto=UDP')"
    },
    "3": {
        "name": "10th-Grade Educational Study Helper",
        "weights": "gpt1_student.pth",
        "dataset": "input_student.txt",
        "prompt_hint": "Ask study questions (e.g. 'what is photosynthesis', 'what is a quadratic equation')"
    },
    "4": {
        "name": "Collins Dictionary Word Lookup",
        "weights": "gpt1_dictionary.pth",
        "dataset": "input_dictionary.txt",
        "prompt_hint": "Enter word to search (e.g. 'ephemeral', 'gregarious', 'mitigate')"
    }
}

def load_mode(choice):
    mode_info = MODES[choice]
    print(f"\nLoading {mode_info['name']}...")
    
    # Check dependencies
    if not os.path.exists(mode_info['dataset']):
        print(f"Error: Dataset {mode_info['dataset']} not found.")
        return None, None, None
    if not os.path.exists(mode_info['weights']):
        print(f"Error: Model weights {mode_info['weights']} not found. Train the model first.")
        return None, None, None

    # Load dataset to extract vocabulary dynamically
    with open(mode_info['dataset'], 'r', encoding='utf-8') as f:
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

    # Load weights
    model.load_state_dict(torch.load(mode_info['weights'], map_location=device))
    model.eval()
    print("Model successfully loaded and initialized!")
    return model, encode, decode

def run_chat(choice):
    model, encode, decode = load_mode(choice)
    if not model:
        return
    
    mode_info = MODES[choice]
    print("\n" + "="*60)
    print(f"Active Mode: {mode_info['name']}")
    print(f"Prompt Style: {mode_info['prompt_hint']}")
    print("Type 'exit' to return to the main menu.")
    print("="*60)
    
    while True:
        try:
            user_input = input("\nPrompt: ").strip()
            if not user_input:
                continue
            if user_input.lower() == 'exit':
                break
                
            # Process prompt based on model mode
            if choice == "3": # Educational Q&A formatting
                formatted_prompt = f"Question: {user_input.lower()}\nAnswer:"
            elif choice == "4": # Dictionary formatting
                formatted_prompt = f"Word: {user_input.lower()}\n"
            else:
                formatted_prompt = user_input
                
            context = torch.tensor([encode(formatted_prompt)], dtype=torch.long, device=device)
            print("Generating output...")
            generated = model.generate(context, max_new_tokens=200)[0].tolist()
            full_response = decode(generated)
            
            # Post-process response output for cleaner display
            if choice == "3":
                answer_part = full_response.split("Answer:")[1].split("Question:")[0].strip()
                print(f"Answer: {answer_part}")
            elif choice == "4":
                definition_part = full_response.split("Word:")[1].split("Word:")[0].strip()
                print(f"Word: {definition_part}")
            else:
                print(f"\nResponse:\n{full_response}")
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Inference error: {e}")

def main():
    while True:
        print("\n" + "="*50)
        print("         GPT-1 INTEGRATED ASSISTANT")
        print("="*50)
        for k, v in MODES.items():
            print(f" [{k}] {v['name']}")
        print(" [5] Exit Assistant")
        print("="*50)
        
        choice = input("Select a mode: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        elif choice in MODES:
            run_chat(choice)
        else:
            print("Invalid choice, please select again.")

if __name__ == "__main__":
    main()
