import random

# Excerpts showcasing high-quality grammar and step-by-step reasoning
book_passages = [
    # 1. Fiction (Sherlock Holmes - Deductive Reasoning)
    {
        "title": "Sherlock Holmes: The Sign of Three",
        "text": "It is an old maxim of mine that when you have excluded the impossible, whatever remains, however improbable, must be the truth. By eliminating all other factors, we are left with the single logical conclusion. We know that the entry was not made through the door, nor was it made through the window. Therefore, it must have been made through the chimney."
    },
    {
        "title": "Sherlock Holmes: A Study in Scarlet",
        "text": "The observer who has reasoned out one link in a series of incidents should be able to state all the other links. From a drop of water, a logician could infer the possibility of an Atlantic or a Niagara. So all life is a great chain, the nature of which is known whenever we are shown a single link of it."
    },
    
    # 2. Non-Fiction (Thinking, Fast and Slow - Cognitive Reasoning)
    {
        "title": "Thinking, Fast and Slow: System 1 and System 2",
        "text": "System 1 operates automatically and quickly, with little or no effort and no sense of voluntary control. System 2 allocates attention to the effortful mental activities that demand it, including complex computations. Therefore, System 2 is activated when we do something that does not come naturally, requiring focus and deliberate calculation."
    },
    {
        "title": "Thinking, Fast and Slow: The Law of Small Numbers",
        "text": "The law of small numbers states that small samples are highly prone to extreme outcomes. Because of this random variation, we should not draw major conclusions from a small dataset. To achieve statistical reliability, we must increase the sample size to reduce the probability of random errors distorting the truth."
    },
    
    # 3. Non-Fiction (Sapiens - Historical & Scientific Reasoning)
    {
        "title": "Sapiens: The Cognitive Revolution",
        "text": "The Cognitive Revolution enabled Homo sapiens to transmit information about things that do not exist in reality. Consequently, humans can cooperate in extremely large groups by believing in common myths. This ability to create a shared imagination is the primary reason why humans conquered the planet instead of other animals."
    },
    {
        "title": "Sapiens: The Agricultural Revolution",
        "text": "The Agricultural Revolution did not make the lives of average humans easier. Rather, it led to a population explosion and the creation of crowded cities. As a result, it forced individuals to work longer hours in fields, proving that evolutionary success of a species does not always align with individual happiness."
    }
]

def generate_dataset():
    output_path = "input_books.txt"
    dataset_content = ""
    
    # Repeat the passages to build a robust training corpus of reasoning grammar
    for _ in range(350):
        random.shuffle(book_passages)
        for passage in book_passages:
            dataset_content += f"Book: {passage['title']}\nPassage: {passage['text']}\n\n"
            
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(dataset_content)
    print(f"Dataset generated! Good grammar and reasoning text written to {output_path}")

if __name__ == "__main__":
    generate_dataset()
