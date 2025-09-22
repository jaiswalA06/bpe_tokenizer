# Byte Pair Encoding (BPE) Tokenizer  

This project is a **minimal implementation of a Byte Pair Encoding (BPE) tokenizer** written in Python, without using existing tokenization libraries like `tiktoken`.  

It can:  
1. **Train** on a text corpus (`alice.txt`).  
2. **Encode** new text into a list of integer token IDs.  
3. **Decode** token IDs back to the original text (lossless for the training set).  

---

## 📂 Project Structure 
bpe_tokenizer/
│
├── src/
│ ├── tokenizer.py # Implementation of BPETokenizer
│ └── main.py # CLI demo script (train/encode/decode)
│
├── alice.txt # Training corpus (sample from Alice in Wonderland)
├── README.md # Project instructions
└── output.txt # Example output from running main.py

### 1. Clone the repository  

```bash
git clone https://github.com/<your-username>/bpe_tokenizer.git
cd bpe_tokenizer
```

2. Run the demo

```bash
python src/main.py
```

3. Output
The script will:

Train the tokenizer on alice.txt.

Encode and decode a sample sentence.

Save results in output.txt.

4. Example console output:

```bash
Training tokenizer...

Encoding: Alice was beginning to get very tired
Tokens: [3, 7, 14, 22, 5, ...]
Decoded: Alicewasbeginningtogetverytired

Results written to output.txt
```

🧪 Example Corpus (alice.txt)
The provided alice.txt contains paragraphs from Alice’s Adventures in Wonderland by Lewis Carroll, which serves as the training corpus.

📝 Notes
This is a minimal educational BPE tokenizer, not optimized for production use.

Special tokens, regex pre-tokenization, and Unicode corner cases are ignored for simplicity.

