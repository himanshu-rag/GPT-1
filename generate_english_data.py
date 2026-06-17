import random

# A diverse set of general English conversations (Chit-Chat, Greetings, Facts, and Networking)
english_conversations = [
    # Greetings
    {"q": "hello", "a": "Hello! How can I help you today?"},
    {"q": "hi", "a": "Hi there! What can I do for you?"},
    {"q": "how are you", "a": "I am doing well, thank you for asking! How are you?"},
    {"q": "what is your name", "a": "I am a mini GPT-1 language model trained on network concepts and general chat."},
    {"q": "who created you", "a": "I was built using PyTorch based on the GPT-1 architecture proposed by OpenAI."},
    {"q": "good morning", "a": "Good morning! Hope you have a wonderful day ahead."},
    {"q": "good night", "a": "Good night! Sleep well and have sweet dreams."},
    
    # Chit-chat & Hobbies
    {"q": "do you like music", "a": "I don't have ears, but I can read and write lyrics! What kind of music do you like?"},
    {"q": "tell me a joke", "a": "Why do programmers wear glasses? Because they can't C#!"},
    {"q": "what is your favorite food", "a": "I consume electric current and data packets! But I hear pizza is very popular among humans."},
    {"q": "what do you do", "a": "I predict the next character in a sequence to simulate human-like conversations."},
    {"q": "do you sleep", "a": "No, I am a program, so I am awake and ready to chat 24/7!"},
    
    # General Facts
    {"q": "what is the capital of france", "a": "The capital of France is Paris, famous for the Eiffel Tower, art, and fashion."},
    {"q": "what is the sun", "a": "The sun is a star at the center of our solar system that provides heat, light, and energy to Earth."},
    {"q": "what is water", "a": "Water is a transparent chemical compound composed of two hydrogen atoms and one oxygen atom (H2O)."},
    {"q": "what is a computer", "a": "A computer is an electronic device that processes data, performs calculations, and operates based on instructions."},
    {"q": "what is programming", "a": "Programming is the process of writing instructions in a language that computers can execute to perform tasks."},

    # Networking Q&A (retaining the networking knowledge)
    {"q": "what is my ip", "a": "Your IP address is a unique identifier for your device. On a local network, it is usually 192.168.x.x."},
    {"q": "what is tcp", "a": "TCP is a reliable, connection-oriented transport protocol that uses a three-way handshake to guarantee data delivery."},
    {"q": "what is udp", "a": "UDP is a connectionless, lightweight transport protocol used when speed is more important than reliability, like in video games."},
    {"q": "how does dns work", "a": "DNS translates domain names like google.com into numerical IP addresses so browsers can load internet websites."},
    {"q": "what is the osi model", "a": "The OSI model is a 7-layer framework for network communication: Physical, Data Link, Network, Transport, Session, Presentation, Application."},
    {"q": "what is a router", "a": "A router is a Layer 3 device that routes data packets between different networks using IP addresses."},
    {"q": "what is a switch", "a": "A switch is a Layer 2 device that forwards data frames inside a local area network using MAC addresses."},
    {"q": "what is a mac address", "a": "A MAC address is a permanent physical hardware address assigned to a device's network card at the factory."}
]

def generate_dataset():
    output_path = "data/input_english.txt"
    dataset_content = ""
    
    # Repeat the conversation corpus to give the character-level model enough training samples
    for _ in range(200):
        random.shuffle(english_conversations)
        for pair in english_conversations:
            dataset_content += f"Question: {pair['q']}\nAnswer: {pair['a']}\n\n"
            
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(dataset_content)
    print(f"Dataset generated! General English and Networking logs written to {output_path}")

if __name__ == "__main__":
    generate_dataset()
