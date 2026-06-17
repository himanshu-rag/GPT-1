import urllib.request
import xml.etree.ElementTree as ET
import ssl
import os

# Bypass SSL verification for macOS
ssl._create_default_https_context = ssl._create_unverified_context

def fetch_research_papers():
    # Search for Computer Science papers in AI, NI (Networking), SE (Software Engineering), DB (Databases), CR (Cybersecurity), and DC (Cloud Computing)
    query_url = (
        "http://export.arxiv.org/api/query?search_query="
        "cat:cs.AI+OR+cat:cs.NI+OR+cat:cs.SE+OR+cat:cs.DB+OR+cat:cs.CR+OR+cat:cs.DC"
        "&max_results=30"
    )
    
    print("Fetching research papers from arXiv API...")
    output_path = "input_research.txt"
    compiled_text = ""
    
    try:
        req = urllib.request.Request(query_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            
        # Parse XML
        root = ET.fromstring(xml_data)
        
        # arXiv API uses Atom feed namespace
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        entries = root.findall('atom:entry', ns)
        print(f"Successfully retrieved {len(entries)} research papers.")
        
        for entry in entries:
            title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
            summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
            compiled_text += f"Paper Title: {title}\nAbstract: {summary}\n\n"
            
    except Exception as e:
        print(f"Error fetching research papers: {e}")
        return

    if compiled_text:
        # Repeat the corpus to build sufficient volume for the character-level model
        final_content = ""
        for _ in range(50):
            final_content += compiled_text
            
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Research paper dataset saved to {output_path} (Size: {len(final_content)/1024:.1f} KB)")
    else:
        print("Error: No research paper content gathered.")

if __name__ == "__main__":
    fetch_research_papers()
