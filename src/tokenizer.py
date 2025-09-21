# src/tokenizer.py
# Minimal BPE Tokenizer Skeleton

from collections import Counter

class BPETokenizer:
    def __init__(self):
        self.vocab = {}
        self.inverse_vocab = {}
        self.merges = []
        self.vocab_size = 0

    def get_stats(self, corpus):
        """Count frequency of symbol pairs in corpus."""
        pairs = Counter()
        for word in corpus:
            for i in range(len(word)):   # <-- BUG: should be len(word)-1
                pairs[(word[i], word[i+1])] += 1
        return pairs


