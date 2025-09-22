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

git clone https://github.com/<jaiswalaA06>/bpe_tokenizer.git
cd bpe_tokenizer

2. Run the demo
python src/main.py

3. Output
The script will:
    Train the tokenizer on alice.txt.
    Encode and decode a sample sentence.
    Save results in output.txt.
    Results written to output.txt

4. Example Corpus (alice.txt)
The provided alice.txt contains paragraphs from Alice’s Adventures in Wonderland by Lewis Carroll, which serves as the training corpus.

📝 Notes
This is a minimal educational BPE tokenizer, not optimized for production use.
Special tokens, regex pre-tokenization, and Unicode corner cases are ignored for simplicity.

