from datasets import load_dataset
import os

print("Connecting to Hugging Face and streaming OpenAssistant/oasst1...")
compiled_text = ""
target_size = 100 * 1024 * 1024 # 100 MB total

# 1. Load and parse OpenAssistant (oasst1)
try:
    # Stream the dataset to be fast and memory-efficient
    oasst_dataset = load_dataset("OpenAssistant/oasst1", split="train", streaming=True)
    
    # We buffer messages to reconstruct parent-child pairs
    msg_cache = {}
    oasst_pairs = []
    
    print("Reading OpenAssistant rows...")
    count = 0
    for row in oasst_dataset:
        msg_id = row["message_id"]
        parent_id = row["parent_id"]
        text = row["text"].strip()
        role = row["role"]
        lang = row.get("lang", "en")
        
        # We focus on English conversations for better training alignment
        if lang == "en":
            msg_cache[msg_id] = {"text": text, "role": role}
            if parent_id in msg_cache:
                parent = msg_cache[parent_id]
                if parent["role"] == "prompter" and role == "assistant":
                    oasst_pairs.append((parent["text"], text))
            count += 1
            if len(oasst_pairs) >= 4000 or count >= 40000:
                break
                
    for prompt, response in oasst_pairs:
        compiled_text += f"Instruction: {prompt}\nResponse: {response}\n\n"
        
    print(f"Reconstructed {len(oasst_pairs)} conversational pairs from OpenAssistant.")
except Exception as e:
    print(f"Error loading OpenAssistant: {e}")

# 2. Load and parse UltraChat 200k
print("\nConnecting to Hugging Face and streaming HuggingFaceH4/ultrachat_200k...")
try:
    ultrachat_dataset = load_dataset("HuggingFaceH4/ultrachat_200k", split="train_sft", streaming=True)
    
    uc_count = 0
    for row in ultrachat_dataset:
        messages = row.get("messages", [])
        # Extract prompt-response pairs from conversation messages
        for i in range(len(messages) - 1):
            if messages[i]["role"] == "user" and messages[i+1]["role"] == "assistant":
                prompt = messages[i]["content"].strip()
                response = messages[i+1]["content"].strip()
                compiled_text += f"Instruction: {prompt}\nResponse: {response}\n\n"
                uc_count += 1
                if uc_count % 1000 == 0:
                    print(f"Gathered {uc_count} pairs from UltraChat...")
                
        if len(compiled_text.encode('utf-8')) >= target_size or uc_count >= 40000:
            break
            
    print(f"Gathered {uc_count} conversational pairs from UltraChat.")
except Exception as e:
    print(f"Error loading UltraChat: {e}")

# 3. Save compiled text
if compiled_text:
    # Truncate to target size to keep local character-level training fast and balanced
    encoded = compiled_text.encode('utf-8')
    if len(encoded) > target_size:
        compiled_text = encoded[:int(target_size)].decode('utf-8', errors='ignore')
        
    with open("data/input_conversation.txt", "w", encoding="utf-8") as f:
        f.write(compiled_text)
    print(f"\nSaved compiled dataset to data/input_conversation.txt (Size: {len(compiled_text.encode('utf-8'))/1024:.1f} KB)")
else:
    print("\nError: No text was compiled from either dataset.")
