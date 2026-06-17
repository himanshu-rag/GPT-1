import random

# A diverse set of Instruction-Following tasks, FAQs, and Educational Q&As
instruction_qa = [
    # 1. Instruction Following
    {
        "q": "translate 'thank you' to spanish",
        "a": "'Gracias' is the Spanish translation for 'thank you'."
    },
    {
        "q": "list the three primary colors",
        "a": "The three primary colors are red, yellow, and blue. All other colors can be created by mixing these three."
    },
    {
        "q": "extract the name from: hello my name is sarah and i am an engineer",
        "a": "The name extracted from the text is Sarah."
    },
    {
        "q": "reverse the word: python",
        "a": "The reversed form of 'python' is 'nohtyp'."
    },
    
    # 2. General FAQs
    {
        "q": "how do i reset my router",
        "a": "To reset your router, locate the small reset button on the back, press and hold it with a paperclip for 10 seconds, then release. The router will reboot and restore its default factory settings."
    },
    {
        "q": "what is a web cache",
        "a": "A web cache is a temporary storage mechanism that saves copies of web documents (like HTML pages and images) to reduce bandwidth usage and speed up page load times."
    },
    {
        "q": "why is my internet slow",
        "a": "Slow internet can be caused by network congestion, poor Wi-Fi signal strength, router issues, too many connected devices, or issues with your Internet Service Provider (ISP). Try restarting your router first."
    },
    
    # 3. Educational Q&As
    {
        "q": "what is the speed of light",
        "a": "The speed of light in a vacuum is approximately 299,792 kilometers per second (about 186,282 miles per second)."
    },
    {
        "q": "who wrote hamlet",
        "a": "Hamlet was written by the English playwright and poet William Shakespeare between 1599 and 1601."
    },
    {
        "q": "how many continents are there",
        "a": "There are seven continents on Earth: Asia, Africa, North America, South America, Antarctica, Europe, and Australia."
    },
    {
        "q": "what is the capital of japan",
        "a": "The capital of Japan is Tokyo, which is known for its blend of ultramodern style and traditional temples."
    }
]

def generate_dataset():
    output_path = "input_instructions.txt"
    dataset_content = ""
    
    # Repeat the corpus to ensure the character-level model can map the prompts to exact responses
    for _ in range(300):
        random.shuffle(instruction_qa)
        for pair in instruction_qa:
            dataset_content += f"Instruction: {pair['q']}\nResponse: {pair['a']}\n\n"
            
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(dataset_content)
    print(f"Dataset compiled! Instruction-following entries written to {output_path}")

if __name__ == "__main__":
    generate_dataset()
