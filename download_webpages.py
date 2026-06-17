import urllib.request
import json
import ssl
import os

# Bypass SSL verification for macOS issues
ssl._create_default_https_context = ssl._create_unverified_context

topics = [
    "Artificial_intelligence",
    "Computer_science",
    "Internet",
    "World_Wide_Web",
    "Machine_learning",
    "Algorithm"
]

def fetch_wiki_articles():
    output_path = "data/input_web.txt"
    compiled_text = ""
    
    for topic in topics:
        print(f"Fetching Wikipedia article for: {topic}...")
        url = f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&explaintext&redirects=1&titles={topic}"
        
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))
                pages = data['query']['pages']
                for page_id in pages:
                    extract = pages[page_id].get('extract', '')
                    if extract:
                        compiled_text += f"Article Title: {topic.replace('_', ' ')}\nContent:\n{extract}\n\n"
        except Exception as e:
            print(f"Failed to fetch {topic}: {e}")
            
    if compiled_text:
        # Repeat the compiled text to give the character-level model enough training volume
        final_content = ""
        for _ in range(50):
            final_content += compiled_text
            
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Dataset compiled and saved to {output_path} (Size: {len(final_content)/1024:.1f} KB)")
    else:
        print("Error: Could not compile any articles.")

if __name__ == "__main__":
    fetch_wiki_articles()
