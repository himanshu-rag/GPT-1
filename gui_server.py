import http.server
import socketserver
import json
import os
import urllib.parse
import webbrowser
import torch
from gpt1 import GPT1LanguageModel

PORT = 8080
device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'

# 1. Setup tokenizer loader helper
def setup_tokenizer(data_path):
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found.")
        exit(1)
    with open(data_path, 'r', encoding='utf-8') as f:
        text = f.read()
    chars = sorted(list(set(text)))
    vocab_size = len(chars)
    stoi = { ch:i for i,ch in enumerate(chars) }
    itos = { i:ch for i,ch in enumerate(chars) }
    encode = lambda s: [stoi[c] for c in s if c in stoi]
    decode = lambda l: ''.join([itos[i] for i in l])
    return vocab_size, stoi, itos, encode, decode

# Load setups
print("Loading Academic model vocabulary...")
acad_vocab_size, acad_stoi, acad_itos, acad_encode, acad_decode = setup_tokenizer("data/input_academic.txt")

print("Loading FineWeb model vocabulary...")
fw_vocab_size, fw_stoi, fw_itos, fw_encode, fw_decode = setup_tokenizer("data/input_fineweb.txt")

print("Loading Chat Assistant vocabulary...")
chat_vocab_size, chat_stoi, chat_itos, chat_encode, chat_decode = setup_tokenizer("data/input_conversation.txt")

wiki_loaded = False
if os.path.exists("data/input_wikipedia.txt"):
    print("Loading Wikipedia model vocabulary...")
    wiki_vocab_size, wiki_stoi, wiki_itos, wiki_encode, wiki_decode = setup_tokenizer("data/input_wikipedia.txt")
    wiki_loaded = True

books_loaded = False
if os.path.exists("data/input_books.txt"):
    print("Loading Books model vocabulary...")
    books_vocab_size, books_stoi, books_itos, books_encode, books_decode = setup_tokenizer("data/input_books.txt")
    books_loaded = True

basic_loaded = False
if os.path.exists("data/input_basic.txt"):
    print("Loading Basic Knowledge model vocabulary...")
    basic_vocab_size, basic_stoi, basic_itos, basic_encode, basic_decode = setup_tokenizer("data/input_basic.txt")
    basic_loaded = True

maths_loaded = False
if os.path.exists("data/input_maths.txt"):
    print("Loading Mathematics model vocabulary...")
    maths_vocab_size, maths_stoi, maths_itos, maths_encode, maths_decode = setup_tokenizer("data/input_maths.txt")
    maths_loaded = True

# 2. Initialize and load models
def load_model(vocab_size, weights_path, block_size, n_embd=128, n_head=4, n_layer=4):
    model = GPT1LanguageModel(
        vocab_size=vocab_size,
        n_embd=n_embd,
        n_head=n_head,
        n_layer=n_layer,
        block_size=block_size,
        dropout=0.0,
        device=device
    ).to(device)
    if os.path.exists(weights_path):
        try:
            checkpoint = torch.load(weights_path, map_location=device)
            checkpoint_vocab = checkpoint['token_embedding_table.weight'].shape[0]
            if checkpoint_vocab != vocab_size:
                print(f"Vocab mismatch for {weights_path}: Checkpoint ({checkpoint_vocab}) vs Server ({vocab_size}). Adapting weights...")
                model_dict = model.state_dict()
                min_vocab = min(checkpoint_vocab, vocab_size)
                model_dict['token_embedding_table.weight'][:min_vocab] = checkpoint['token_embedding_table.weight'][:min_vocab]
                model_dict['lm_head.weight'][:min_vocab] = checkpoint['lm_head.weight'][:min_vocab]
                model_dict['lm_head.bias'][:min_vocab] = checkpoint['lm_head.bias'][:min_vocab]
                for k, v in checkpoint.items():
                    if k not in ['token_embedding_table.weight', 'lm_head.weight', 'lm_head.bias']:
                        model_dict[k] = v
                model.load_state_dict(model_dict)
            else:
                model.load_state_dict(checkpoint)
            print(f"Loaded weights from {weights_path}")
        except Exception as e:
            print(f"Error loading {weights_path}: {e}")
    else:
        print(f"Warning: {weights_path} not found. Running with uninitialized weights.")
    model.eval()
    return model

print("Initializing Academic model...")
academic_model = load_model(acad_vocab_size, 'weights/gpt1_academic.pth', block_size=256)

print("Initializing FineWeb model...")
fineweb_model = load_model(fw_vocab_size, 'weights/gpt1_fineweb.pth', block_size=256)

print("Initializing Chat Assistant model...")
chat_model = load_model(chat_vocab_size, 'weights/gpt1_conversation.pth', block_size=256)

# Router dictionary for requests
models_config = {
    "academic": {
        "model": academic_model,
        "encode": acad_encode,
        "decode": acad_decode,
        "stoi": acad_stoi
    },
    "fineweb": {
        "model": fineweb_model,
        "encode": fw_encode,
        "decode": fw_decode,
        "stoi": fw_stoi
    },
    "chat": {
        "model": chat_model,
        "encode": chat_encode,
        "decode": chat_decode,
        "stoi": chat_stoi
    }
}

if wiki_loaded:
    print("Initializing Wikipedia model...")
    wikipedia_model = load_model(wiki_vocab_size, 'weights/gpt1_wikipedia.pth', block_size=256)
    models_config["wikipedia"] = {
        "model": wikipedia_model,
        "encode": wiki_encode,
        "decode": wiki_decode,
        "stoi": wiki_stoi
    }

if books_loaded:
    print("Initializing Literature Books model...")
    books_model = load_model(books_vocab_size, 'weights/gpt1_books.pth', block_size=512)
    models_config["books"] = {
        "model": books_model,
        "encode": books_encode,
        "decode": books_decode,
        "stoi": books_stoi
    }

if basic_loaded:
    print("Initializing Basic Knowledge model...")
    basic_model = load_model(basic_vocab_size, 'weights/gpt1_basic.pth', block_size=256, n_embd=192, n_head=6, n_layer=6)
    models_config["basic"] = {
        "model": basic_model,
        "encode": basic_encode,
        "decode": basic_decode,
        "stoi": basic_stoi
    }

if maths_loaded:
    print("Initializing Mathematics model...")
    maths_model = load_model(maths_vocab_size, 'weights/gpt1_maths.pth', block_size=512, n_embd=256, n_head=8, n_layer=8)
    models_config["maths"] = {
        "model": maths_model,
        "encode": maths_encode,
        "decode": maths_decode,
        "stoi": maths_stoi
    }

def classify_prompt(prompt):
    p_lower = prompt.lower().strip()
    
    if books_loaded and (p_lower.startswith("book:") or "sherlock" in p_lower or "holmes" in p_lower or "frankenstein" in p_lower or "dracula" in p_lower or "literature" in p_lower):
        return "books"
        
    if wiki_loaded and (p_lower.startswith("article title:") or p_lower.startswith("article:") or "wikipedia" in p_lower or "encyclopedia" in p_lower):
        return "wikipedia"
    
    # Maths: route all math-related topics to maths model
    maths_triggers = [
        "theorem", "formula", "equation", "algebra", "geometry", "trigonometry",
        "arithmetic", "calculus", "polynomial", "quadratic", "linear equation",
        "pythagoras", "pythagorean", "sin", "cos", "tan", "cosine", "sine",
        "hcf", "lcm", "prime factor", "factoris", "factori",
        "perimeter", "area of", "volume of", "surface area",
        "triangle", "rectangle", "square", "circle", "parallelogram", "trapezium",
        "probability", "statistics", "mean", "median", "mode",
        "ratio", "proportion", "percentage", "profit", "loss", "interest",
        "exponent", "logarithm", "square root", "cube root",
        "bodmas", "pemdas", "arithmetic progression", "ap formula",
        "coordinate", "distance formula", "midpoint", "slope",
        "divisibility", "remainder theorem", "factor theorem",
        "discriminant", "roots of", "sum of roots", "product of roots",
        "congruent", "similar triangle", "bpt", "basic proportionality",
        "simple interest", "compound interest", "discount",
        "mensuration", "heron", "frustum", "cylinder", "cone", "sphere",
        "class 10", "class 9", "class 8", "maths", "math", "mathematics",
        "what is 1 +", "what is 2 +", "solve", "calculate", "find the value",
    ]
    if maths_loaded and any(k in p_lower for k in maths_triggers):
        return "maths"

    # Basic knowledge: greetings, simple definitions, numbers, colors, shapes, animals, grammar
    basic_triggers = [
        "hello", "hi", "hey", "good morning", "good afternoon", "good evening", "good night",
        "how are you", "what is your name", "who are you", "thank you", "thanks", "bye", "goodbye",
        "what is the meaning of", "what does", "define ", "explain the word",
        "what color", "what are the colors", "primary color",
        "what are the days", "days of the week", "months of the year",
        "how many days", "how many months", "how many letters", "how many planets", "how many continents",
        "opposite of", "antonym of", "synonym of",
        "what is a noun", "what is a verb", "what is an adjective", "what is grammar",
        "plus", "minus", "times", "divided by", "multiplied by",
        "what animal", "tell me about dogs", "tell me about cats", "what is a dog", "what is a cat",
        "what is the sun", "what is the moon", "why is the sky", "why do we",
        "what do you use to", "what makes", "can you see", "is a tomato",
        "even number", "odd number",
    ]
    if basic_loaded and any(k in p_lower for k in basic_triggers):
        return "basic"
        
    if p_lower.startswith("source: arxiv") or p_lower.startswith("source: semantic scholar") or p_lower.startswith("source: pubmed"):
        return "academic"
    if p_lower.startswith("instruction:"):
        return "chat"
    if p_lower.startswith("the internet is") or p_lower.startswith("technology has") or p_lower.startswith("once upon a time"):
        return "fineweb"
        
    academic_keywords = [
        "arxiv", "abstract", "paper", "study", "research", "journal", "citation", 
        "algorithm", "methodology", "dataset", "deep learning for", "neural network",
        "scientific", "experiment", "evaluation", "results of", "proposed method"
    ]
    if any(k in p_lower for k in academic_keywords):
        return "academic"
        
    # Check for general encyclopedic/factual questions for Wikipedia (if loaded)
    if wiki_loaded:
        wiki_question_keywords = ["history of", "tell me about", "who was", "where is", "when did", "biography", "capital of", "population of"]
        if any(k in p_lower for k in wiki_question_keywords):
            return "wikipedia"
        
    chat_keywords = [
        "how to", "write a", "explain", "who is", "what is", "where is", "why does",
        "can you", "please", "question", "tell me", "solve",
        "translate", "summarize", "help me", "ai", "assistant", "chat", "instruction"
    ]
    if any(k in p_lower for k in chat_keywords) or "?" in p_lower or p_lower.startswith(("what", "how", "who", "why", "where", "can", "could", "would", "should", "will", "is", "are")):
        return "chat"
        
    return "fineweb"

class GeneratorHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Suppress logging to keep output clean
        pass

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open("index.html", "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404, "File Not Found")

    def do_POST(self):
        if self.path == "/generate":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                prompt = data.get("prompt", "")
                max_tokens = int(data.get("max_tokens", 250))
                model_type = data.get("model_type", "fineweb")
                
                # Auto detect model if requested
                selected_model = model_type
                if model_type == "auto":
                    selected_model = classify_prompt(prompt)
                    print(f"Auto-classified prompt to: '{selected_model}'")
                
                # Limit tokens to avoid server blocking too long
                max_tokens = min(max_tokens, 500)
                
                print(f"Generating for model: '{selected_model}' (requested: '{model_type}') | prompt: '{prompt[:40]}...' | tokens: {max_tokens}")
                
                if selected_model not in models_config:
                    selected_model = "fineweb"
                
                config = models_config[selected_model]
                model = config["model"]
                encode = config["encode"]
                decode = config["decode"]
                stoi = config["stoi"]
                
                # Format prompt based on model type
                if selected_model in ("chat", "basic"):
                    if not prompt.strip().startswith("Instruction:"):
                        formatted_prompt = f"Instruction: {prompt}\nResponse:"
                    else:
                        formatted_prompt = prompt
                else:
                    formatted_prompt = prompt
                
                # Encode and generate
                encoded_prompt = encode(formatted_prompt)
                if not encoded_prompt:
                    encoded_prompt = [stoi.get(' ', 0)]
                
                context = torch.tensor([encoded_prompt], dtype=torch.long, device=device)
                
                with torch.no_grad():
                    # If chat model, limit generate tokens slightly to keep responses short & snappy
                    tokens_to_gen = min(max_tokens, 150) if selected_model == "chat" else max_tokens
                    generated_seq = model.generate(context, max_new_tokens=tokens_to_gen)[0].tolist()
                
                output_text = decode(generated_seq)
                
                # Post-process response output for chat/basic
                raw_output = output_text
                if selected_model in ("chat", "basic"):
                    if "Response:" in output_text:
                        parts = output_text.split("Response:")
                        res = parts[1].strip()
                        if "Instruction:" in res:
                            res = res.split("Instruction:")[0].strip()
                        output_text = res if res.strip() else raw_output
                    else:
                        cleaned = output_text.replace(formatted_prompt, "").strip()
                        output_text = cleaned if cleaned else raw_output
                
                # Safety net: never return empty output
                if not output_text.strip():
                    output_text = raw_output if raw_output.strip() else "[Model generated no output. Try a different prompt or more tokens.]"
                
                # Send JSON response
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                response = {
                    "output": output_text,
                    "model_used": selected_model
                }
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
            except Exception as e:
                print(f"Error handling request: {e}")
                self.send_response(500)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        else:
            self.send_error(404, "Not Found")

def run_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), GeneratorHandler) as httpd:
        print(f"Server started at http://localhost:{PORT}")
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

if __name__ == "__main__":
    run_server()
