from datasets import load_dataset
import os

print("Connecting to Hugging Face and streaming HuggingFaceFW/fineweb (sample-10BT)...")
try:
    dataset = load_dataset("HuggingFaceFW/fineweb", name="sample-10BT", split="train", streaming=True)
    
    target_size = 1.5 * 1024 * 1024 # Target 1.5MB of text
    collected_text = ""
    count = 0
    
    for row in dataset:
        collected_text += row["text"] + "\n\n"
        count += 1
        if count % 100 == 0:
            print(f"Gathered {len(collected_text.encode('utf-8'))/1024:.1f} KB of text...")
        if len(collected_text.encode('utf-8')) >= target_size:
            break
            
    with open("data/input_fineweb.txt", "w", encoding="utf-8") as f:
        f.write(collected_text)
        
    print(f"Successfully downloaded and saved {len(collected_text.encode('utf-8'))/1024/1024:.2f} MB of FineWeb text to data/input_fineweb.txt")
except Exception as e:
    print(f"Error streaming FineWeb: {e}")
