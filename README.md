# GPT-1 from Scratch (Shakespeare)

This folder contains a fully functional, mini GPT-1 decoder-only Transformer built from scratch using PyTorch. The model has been trained for 9,000 steps on the Tiny Shakespeare dataset.

## Folder Contents
* `gpt1.py`: The core Transformer architecture (Attention, Multi-Head Attention, Feed-Forward, LayerNorm, Blocks).
* `train.py`: The pipeline for downloading the dataset, tokenizing it, training the model, and saving the weights.
* `generate.py`: The interactive script to generate text using the trained weights.
* `input.txt`: The downloaded dataset (Tiny Shakespeare).
* `gpt1_shakespeare.pth`: The trained model weights (saved after 9,000 steps, validation loss: `1.51`).

---

## How to Resume Anytime

Open your terminal and navigate to this folder:
```bash
cd ~/Desktop/GPT-1
```

### 1. Generate Text (Interactive)
To prompt the model and generate text using your trained weights, run:
```bash
python3 generate.py
```
*It will ask you to enter a starting prompt (e.g., `ROMEO:` or `KING:`), and then it will generate Shakespeare-like dialogue.*

### 2. Continue Training
If you want to train it further (e.g., to 12,000 steps or more):
1. Open `train.py` and increase `max_iters` (e.g., set `max_iters = 12000`).
2. Run the training script:
   ```bash
   python3 -u train.py
   ```
*It will automatically load `input.txt`, resume training on your GPU/CPU, and save the updated weights.*
