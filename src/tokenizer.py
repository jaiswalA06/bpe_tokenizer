# src/tokenizer.py
# Minimal BPE Tokenizer Skeleton

class BPETokenizer:
    def __init__(self):
        self.vocab = {}
        self.inverse_vocab = {}
        self.merges = []
        self.vocab_size = 0
