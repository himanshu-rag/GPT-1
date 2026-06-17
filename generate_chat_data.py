import random

chat_qa = [
    # 1. Greetings
    {"q": "hello", "a": "Hello! How can I help you today?"},
    {"q": "hi", "a": "Hi there! What can I assist you with?"},
    {"q": "hey", "a": "Hey! How can I help you?"},
    {"q": "hello there", "a": "Hello there! How can I help you today?"},
    {"q": "greetings", "a": "Greetings! How may I assist you?"},
    
    # 2. Small Talk
    {"q": "how are you", "a": "I am doing well, thank you for asking! How are you?"},
    {"q": "how are you doing", "a": "I am doing great! How can I assist you today?"},
    {"q": "who are you", "a": "I am your local GPT-1 Assistant, trained on custom datasets."},
    {"q": "what is your name", "a": "I am Siri Assistant, a mini GPT-1 language model."},
    {"q": "what can you do", "a": "I can chat, translate words, reverse text, and answer basic questions!"},
    {"q": "thank you", "a": "You're very welcome! Let me know if you need anything else."},
    {"q": "thanks", "a": "Anytime! Let me know if there's anything else I can do for you."},
    
    # 3. Core Instructions
    {"q": "translate 'thank you' to spanish", "a": "'Gracias' is the Spanish translation for 'thank you'."},
    {"q": "list the three primary colors", "a": "The three primary colors are red, yellow, and blue. All other colors can be created by mixing these three."},
    {"q": "extract the name from: hello my name is sarah and i am an engineer", "a": "The name extracted from the text is Sarah."},
    {"q": "reverse the word: python", "a": "The reversed form of 'python' is 'nohtyp'."},
    {"q": "how do i reset my router", "a": "To reset your router, locate the small reset button on the back, press and hold it with a paperclip for 10 seconds, then release. The router will reboot and restore its default factory settings."},
    {"q": "what is a web cache", "a": "A web cache is a temporary storage mechanism that saves copies of web documents (like HTML pages and images) to reduce bandwidth usage and speed up page load times."},
    {"q": "why is my internet slow", "a": "Slow internet can be caused by network congestion, poor Wi-Fi signal strength, router issues, too many connected devices, or issues with your Internet Service Provider (ISP). Try restarting your router first."},
    {"q": "what is the speed of light", "a": "The speed of light in a vacuum is approximately 299,792 kilometers per second (about 186,282 miles per second)."},
    {"q": "who wrote hamlet", "a": "Hamlet was written by the English playwright and poet William Shakespeare between 1599 and 1601."},
    {"q": "how many continents are there", "a": "There are seven continents on Earth: Asia, Africa, North America, South America, Antarctica, Europe, and Australia."},
    {"q": "what is the capital of japan", "a": "The capital of Japan is Tokyo, which is known for its blend of ultramodern style and traditional temples."}
]

def generate_dataset():
    output_path = "data/input_chat.txt"
    dataset_content = ""
    
    # Shuffle and repeat the dataset 350 times to build a compact 700KB conversational model training set
    for _ in range(350):
        random.shuffle(chat_qa)
        for pair in chat_qa:
            dataset_content += f"Instruction: {pair['q']}\nResponse: {pair['a']}\n\n"
            
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(dataset_content)
    print(f"Conversational dataset compiled! {len(chat_qa)} unique pairs repeated to create {output_path} ({len(dataset_content)/1024:.1f} KB)")

if __name__ == "__main__":
    generate_dataset()
