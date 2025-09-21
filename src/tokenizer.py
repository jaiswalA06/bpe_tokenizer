from collections import Counter

class BPETokenizer:
    def __init__(self):
        self.vocab = {}
        self.inverse_vocab = {}
        self.merges = []
        self.vocab_size = 0

    def get_stats(self, corpus):
        pairs = Counter()
        for word in corpus:
            for i in range(len(word)-1):
                pairs[(word[i], word[i+1])] += 1
        return pairs

    def merge_vocab(self, pair, corpus):
        """Merge the most frequent pair in the corpus."""
        new_corpus = []
        replacement = "".join(pair)
        for word in corpus:
            new_word, i = [], 0
            while i < len(word):
                if i < len(word)-1 and (word[i], word[i+1]) == pair:
                    new_word.append(replacement)
                    
                else:
                    new_word.append(word[i])
                    i += 1
            new_corpus.append(new_word)
        return new_corpus

    def train(self, text, vocab_size=50):
        corpus = [list(word) for word in text.strip().split()]
        self.vocab_size = vocab_size
        for _ in range(vocab_size):
            pairs = self.get_stats(corpus)
            if not pairs: break
            best = max(pairs, key=pairs.get)
            corpus = self.merge_vocab(best, corpus)
            self.merges.append(best)
