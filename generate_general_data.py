import urllib.request
import json
import ssl
import os

# Bypass SSL verification for macOS
ssl._create_default_https_context = ssl._create_unverified_context

# 1. Wikipedia General Articles (representing Wikipedia source)
wiki_topics = ["History", "Geography", "Art", "Science"]

# 2. Project Gutenberg Classics (representing Gutenberg source)
gutenberg_books = {
    "Frankenstein": "https://www.gutenberg.org/files/84/84-0.txt",
    "Pride and Prejudice": "https://www.gutenberg.org/files/1342/1342-0.txt"
}

# 3. Web Blogs / Public Documents (representing Common Crawl & Internet Archive)
web_content = """
Blog Post: The Future of Remote Work
The landscape of professional work has shifted dramatically over the past decade. Remote work, once considered a rare luxury, has now become a standard operating model for companies worldwide. Organizations have realized that productivity does not depend on physical presence in an office. With high-speed internet, video conferencing tools, and collaborative software, teams can synchronize seamlessly across different time zones.

Public Archive Document: The History of the Printing Press
The printing press was invented by Johannes Gutenberg in the Holy Roman Empire around 1440. Gutenberg's key innovation was the development of movable type, which allowed individual letters to be cast in metal and arranged to print text. This revolutionized the spread of information in Europe, making books affordable and rapidly increasing literacy rates across all social classes.
"""

def fetch_data():
    output_path = "input_general.txt"
    compiled_text = ""
    
    # Fetch Wikipedia data
    for topic in wiki_topics:
        print(f"Fetching Wikipedia article: {topic}...")
        url = f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&explaintext&redirects=1&titles={topic}"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))
                pages = data['query']['pages']
                for page_id in pages:
                    extract = pages[page_id].get('extract', '')
                    if extract:
                        compiled_text += f"\n[WIKIPEDIA: {topic}]\n{extract[:15000]}\n" # Take first 15KB of each
        except Exception as e:
            print(f"Failed to fetch wiki {topic}: {e}")
            
    # Fetch Gutenberg data
    for name, url in gutenberg_books.items():
        print(f"Fetching Project Gutenberg: {name}...")
        try:
            with urllib.request.urlopen(url) as response:
                book_text = response.read().decode('utf-8', errors='ignore')
                # Take a 25KB chunk from the middle of the book to avoid metadata
                start_char = len(book_text) // 3
                compiled_text += f"\n[GUTENBERG: {name}]\n{book_text[start_char:start_char+25000]}\n"
        except Exception as e:
            print(f"Failed to fetch book {name}: {e}")
            
    # Add Web Archive / Common Crawl data
    compiled_text += f"\n[COMMON_CRAWL & ARCHIVE]\n{web_content}\n"
    
    if compiled_text:
        # Repeat the corpus to build sufficient volume
        final_content = ""
        for _ in range(15):
            final_content += compiled_text
            
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"General Text dataset saved to {output_path} (Size: {len(final_content)/1024:.1f} KB)")
    else:
        print("Error: No content gathered.")

if __name__ == "__main__":
    fetch_data()
