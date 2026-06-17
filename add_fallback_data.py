import random

# A list of random/out-of-domain prompts and the fallback response
fallback_response = "I am a specialized GPT-1 model trained only on Shakespeare, Networking, 10th-grade subjects, and Collins Dictionary. I do not have information about that topic."

random_prompts = [
    "who is pikachu",
    "what is pokemon",
    "who is batman",
    "tell me about marvel",
    "what is football",
    "how to make coffee",
    "what is a car",
    "who is spider-man",
    "tell me a story about space",
    "what is minecraft",
    "what is youtube",
    "who is harry potter",
    "what is chocolate",
    "what is a smartphone",
    "tell me about netflix",
    "who is iron man",
    "what is pizza",
    "how to play guitar",
    "what is the weather like",
    "what is an apple phone",
    "who is the president",
    "what is music today",
    "tell me about games",
    "what is a cartoon"
]

def append_fallback():
    dataset_path = "input_master.txt"
    if not os.path.exists(dataset_path):
        print("Error: input_master.txt not found. Run merge_datasets.py first.")
        return

    fallback_text = ""
    # Repeat the fallback pairs to make the model memorize this boundary behavior
    for _ in range(200):
        random.shuffle(random_prompts)
        for prompt in random_prompts:
            fallback_text += f"Question: {prompt}\nAnswer: {fallback_response}\n\n"

    with open(dataset_path, "a", encoding="utf-8") as f:
        f.write("\n\n" + fallback_text)
    print(f"Appended fallback training data to input_master.txt")

import os
if __name__ == "__main__":
    append_fallback()
