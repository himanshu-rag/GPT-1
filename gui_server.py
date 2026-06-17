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

# 2. Initialize and load models
def load_model(vocab_size, weights_path, block_size):
    model = GPT1LanguageModel(
        vocab_size=vocab_size,
        n_embd=128,
        n_head=4,
        n_layer=4,
        block_size=block_size,
        dropout=0.0,
        device=device
    ).to(device)
    if os.path.exists(weights_path):
        model.load_state_dict(torch.load(weights_path, map_location=device))
        print(f"Loaded weights from {weights_path}")
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
                
                # Limit tokens to avoid server blocking too long
                max_tokens = min(max_tokens, 500)
                
                print(f"Generating for model: '{model_type}' | prompt: '{prompt[:40]}...' | tokens: {max_tokens}")
                
                if model_type not in models_config:
                    model_type = "fineweb"
                
                config = models_config[model_type]
                model = config["model"]
                encode = config["encode"]
                decode = config["decode"]
                stoi = config["stoi"]
                
                # Format prompt based on model type
                if model_type == "chat":
                    formatted_prompt = f"Instruction: {prompt}\nResponse:"
                else:
                    formatted_prompt = prompt
                
                # Encode and generate
                encoded_prompt = encode(formatted_prompt)
                if not encoded_prompt:
                    encoded_prompt = [stoi.get(' ', 0)]
                
                context = torch.tensor([encoded_prompt], dtype=torch.long, device=device)
                
                with torch.no_grad():
                    # If chat model, limit generate tokens slightly to keep responses short & snappy
                    tokens_to_gen = min(max_tokens, 150) if model_type == "chat" else max_tokens
                    generated_seq = model.generate(context, max_new_tokens=tokens_to_gen)[0].tolist()
                
                output_text = decode(generated_seq)
                
                # Post-process response output for chat
                if model_type == "chat":
                    if "Response:" in output_text:
                        parts = output_text.split("Response:")
                        res = parts[1].strip()
                        if "Instruction:" in res:
                            res = res.split("Instruction:")[0].strip()
                        output_text = res
                    else:
                        # Fallback if Response: tag was somehow stripped or missing
                        output_text = output_text.replace(formatted_prompt, "").strip()
                
                # Send JSON response
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                response = {"output": output_text}
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
