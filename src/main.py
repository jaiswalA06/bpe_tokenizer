import os
from tokenizer import BPETokenizer

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    corpus_file = os.path.join(base_dir, "alice.txt")
    output_file = os.path.join(base_dir, "output.txt")

    with open(corpus_file, "r") as f: 
        text = f.read()

    tokenizer = BPETokenizer()
    tokenizer.train(text, vocab_size=50)

    sample = "Alice was beginning to get very tired"
    encoded = tokenizer.encode(sample)
    decoded = tokenizer.decode(encoded)

    with open(output_file, "w") as out: 
        out.write("Original: " + sample + "\n")
        out.write("Encoded: " + str(encoded) + "\n")
        out.write("Decoded: " + decoded + "\n")

if __name__ == "__main__":
    main()
