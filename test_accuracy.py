import torch
import os
from gpt1 import GPT1LanguageModel

# Model config
block_size = 128
n_embd = 128
n_head = 4
n_layer = 4
dropout = 0.0
device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'

def test_model(model_weights, dataset_file, test_cases, is_dict=False):
    print("\n" + "="*80)
    print(f"TESTING MODEL: {model_weights}")
    print("="*80)
    
    # Load vocab
    with open(dataset_file, 'r', encoding='utf-8') as f:
        text = f.read()
    chars = sorted(list(set(text)))
    vocab_size = len(chars)
    stoi = { ch:i for i,ch in enumerate(chars) }
    itos = { i:ch for i,ch in enumerate(chars) }
    encode = lambda s: [stoi[c] for c in s if c in stoi]
    decode = lambda l: ''.join([itos[i] for i in l])
    
    # Load model
    model = GPT1LanguageModel(
        vocab_size=vocab_size,
        n_embd=n_embd,
        n_head=n_head,
        n_layer=n_layer,
        block_size=block_size,
        dropout=dropout,
        device=device
    ).to(device)
    
    model.load_state_dict(torch.load(model_weights, map_location=device))
    model.eval()
    
    for q in test_cases:
        if is_dict:
            prompt = f"Word: {q}\n"
        else:
            prompt = f"Question: {q}\nAnswer:"
            
        context = torch.tensor([encode(prompt)], dtype=torch.long, device=device)
        generated = model.generate(context, max_new_tokens=150)[0].tolist()
        output = decode(generated)
        
        # Format printing
        if is_dict:
            clean_output = output.split("Word:")[1].split("Word:")[0].strip()
            print(f"Search Word: '{q}'\n{clean_output}\n")
        else:
            clean_output = output.split("Answer:")[1].split("Question:")[0].strip()
            print(f"Q: {q}\nA: {clean_output}\n")

# 1. Test 10th-grade Student Model
test_model(
    model_weights="weights/gpt1_student.pth",
    dataset_file="data/input_student.txt",
    test_cases=[
        "what is a quadratic equation",
        "what are newton's laws of motion"
    ]
)

# 2. Test English / Networking Model
test_model(
    model_weights="weights/gpt1_english.pth",
    dataset_file="data/input_english.txt",
    test_cases=[
        "how does dns work"
    ]
)

# 3. Test Collins Dictionary Model
test_model(
    model_weights="weights/gpt1_dictionary.pth",
    dataset_file="data/input_dictionary.txt",
    test_cases=[
        "juxtaposition"
    ],
    is_dict=True
)
