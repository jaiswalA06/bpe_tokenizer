import os
from tokenizer import BPETokenizer

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    corpus_file = os.path.join(base_dir, "alice.txt")
    output_file = os.path.join(base_dir, "output.txt")

    with open(corpus_file, "r", encoding="utf-8") as f: 
        text = f.read()

    tokenizer = BPETokenizer()
    print("Training tokenizer...")
    tokenizer.train(text, vocab_size=50)

    sample = "Alice was beginning to get very tired"
    print(f"\nEncoding: {sample}")
    encoded = tokenizer.encode(sample)
    print("Tokens:", encoded)

    decoded = tokenizer.decode(encoded)
    print("Decoded:", decoded)

    with open(output_file, "w", encoding="utf-8") as out: 
        out.write("=== BPE Tokenizer Demo ===\n")
        out.write(f"Original: {sample}\n")
        out.write(f"Encoded: {encoded}\n")
        out.write(f"Decoded: {decoded}\n")

    print(f"\nResults written to {output_file}")

if __name__ == "__main__":
    main()
