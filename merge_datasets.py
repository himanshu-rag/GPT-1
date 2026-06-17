import os

def merge_all():
    master_text = ""
    
    # 1. Shakespeare (Take first 200KB to keep it balanced)
    if os.path.exists("input.txt"):
        print("Adding Shakespeare data...")
        with open("input.txt", 'r', encoding='utf-8') as f:
            master_text += f.read()[:200000] + "\n\n"
            
    # 2. Networking Concepts & RFCs (Add first 200KB)
    if os.path.exists("input_networking.txt"):
        print("Adding Networking data...")
        with open("input_networking.txt", 'r', encoding='utf-8') as f:
            master_text += f.read()[:200000] + "\n\n"
            
    # 3. IDS Logs (Add first 200KB)
    if os.path.exists("input_ids.txt"):
        print("Adding Network Intrusion Logs...")
        with open("input_ids.txt", 'r', encoding='utf-8') as f:
            master_text += f.read()[:200000] + "\n\n"
            
    # 4. 10th-Grade Tutor Q&A (Add entire dataset)
    if os.path.exists("input_student.txt"):
        print("Adding 10th-Grade Curriculum Q&As...")
        with open("input_student.txt", 'r', encoding='utf-8') as f:
            master_text += f.read() + "\n\n"
            
    # 5. Collins Dictionary (Add entire dataset)
    if os.path.exists("input_dictionary.txt"):
        print("Adding Dictionary Definitions...")
        with open("input_dictionary.txt", 'r', encoding='utf-8') as f:
            master_text += f.read() + "\n\n"
            
    output_path = "input_master.txt"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(master_text)
    print(f"\nSuccessfully merged all datasets! Saved to {output_path} (Size: {len(master_text)/1024:.1f} KB)")

if __name__ == "__main__":
    merge_all()
