from datasets import load_dataset
import os

print("Connecting to Hugging Face and streaming wikimedia/wikipedia (20231101.en)...")
try:
    dataset = load_dataset("wikimedia/wikipedia", "20231101.en", split="train", streaming=True)
    
    target_size = 20 * 1024 * 1024 # Target 20MB of text
    collected_text = ""
    count = 0
    
    for row in dataset:
        title = row["title"]
        text = row["text"]
        collected_text += f"Article Title: {title}\nContent: {text}\n\n"
        count += 1
        if count % 100 == 0:
            print(f"Gathered {len(collected_text.encode('utf-8'))/1024/1024:.2f} MB of Wikipedia articles...")
        if len(collected_text.encode('utf-8')) >= target_size:
            break
            
    output_path = "data/input_wikipedia.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(collected_text)
        
    print(f"Successfully downloaded and saved {len(collected_text.encode('utf-8'))/1024/1024:.2f} MB of Wikipedia text to {output_path}")
except Exception as e:
    print(f"Error streaming Wikipedia: {e}")
