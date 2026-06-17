import random

# A set of advanced English words and definitions in the style of Collins Dictionary
dictionary_entries = [
    {"word": "aberration", "pos": "noun", "def": "a departure from what is normal, usual, or expected, typically one that is unwelcome."},
    {"word": "benevolent", "pos": "adjective", "def": "well-meaning, kindly, and serving a charitable rather than a profit-making purpose."},
    {"word": "cacophony", "pos": "noun", "def": "a harsh, discordant mixture of sounds, noises, or voices."},
    {"word": "diligent", "pos": "adjective", "def": "having or showing care and conscientiousness in one's work or duties."},
    {"word": "ephemeral", "pos": "adjective", "def": "lasting for a very short time; transient or fleeting in nature."},
    {"word": "fortuitous", "pos": "adjective", "def": "happening by a lucky accident or chance rather than by design."},
    {"word": "gregarious", "pos": "adjective", "def": "of a person fond of company; highly sociable and outgoing."},
    {"word": "harangue", "pos": "noun", "def": "a lengthy and aggressive speech; a loud, critical lecture."},
    {"word": "inevitable", "pos": "adjective", "def": "certain to happen; completely unavoidable and bound to occur."},
    {"word": "juxtaposition", "pos": "noun", "def": "the fact of two things being seen or placed close together with contrasting effect."},
    {"word": "laconical", "pos": "adjective", "def": "using very few words to express what you mean; concise or brief."},
    {"word": "mitigate", "pos": "verb", "def": "to make something bad, painful, or serious less severe, serious, or painful."},
    {"word": "nefarious", "pos": "adjective", "def": "wicked, impious, or criminal; extremely flagrant in wrongdoing."},
    {"word": "ostentatious", "pos": "adjective", "def": "characterized by vulgar or pretentious display; designed to impress or attract notice."},
    {"word": "pragmatic", "pos": "adjective", "def": "dealing with things sensibly and realistically in a way that is based on practical considerations."},
    {"word": "querulous", "pos": "adjective", "def": "complaining in a petulant, whining, or fretful manner."},
    {"word": "resilient", "pos": "adjective", "def": "able to withstand or recover quickly from difficult conditions; strong and elastic."},
    {"word": "scrutinize", "pos": "verb", "def": "to examine or inspect something very closely and thoroughly."},
    {"word": "taciturn", "pos": "adjective", "def": "of a person reserved or uncommunicative in speech; saying little."},
    {"word": "ubiquitous", "pos": "adjective", "def": "present, appearing, or found everywhere at the same time."},
    {"word": "venerable", "pos": "adjective", "def": "accorded a great deal of respect, especially because of age, wisdom, or character."},
    {"word": "wary", "pos": "adjective", "def": "feeling or showing caution about possible dangers or problems; suspicious."},
    {"word": "zealous", "pos": "adjective", "def": "having or showing great energy, enthusiasm, or passion in pursuit of a cause or objective."}
]

def generate_dataset():
    output_path = "input_dictionary.txt"
    dataset_content = ""
    
    # Repeat the dictionary entries to train the character-level model on the definition formats
    for _ in range(300):
        random.shuffle(dictionary_entries)
        for entry in dictionary_entries:
            dataset_content += f"Word: {entry['word']}\nPOS: {entry['pos']}\nDefinition: {entry['def']}\n\n"
            
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(dataset_content)
    print(f"Dataset generated! Structured dictionary definitions written to {output_path}")

if __name__ == "__main__":
    generate_dataset()
