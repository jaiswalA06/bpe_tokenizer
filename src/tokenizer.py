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
            for i in range(len(word) - 1):
                pairs[(word[i], word[i+1])] += 1
        return pairs

    def merge_vocab(self, pair, corpus):
        new_corpus = []
        replacement = "".join(pair)
        for word in corpus:
            new_word, i = [], 0
            while i < len(word):
                if i < len(word)-1 and (word[i], word[i+1]) == pair:
                    new_word.append(replacement)
                    i += 2
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

        # Build vocab
        unique_tokens = set(tok for word in corpus for tok in word)
        self.vocab = {tok: i for i, tok in enumerate(sorted(unique_tokens))}
        self.inverse_vocab = {i: tok for tok, i in self.vocab.items()}

    def encode(self, text):
        words = [list(word) for word in text.strip().split()]
        for pair in self.merges:
            words = self.merge_vocab(pair, words)
        tokens = [self.vocab[token] for word in words for token in word if token in self.vocab]
        return tokens

    def decode(self, token_ids):
        subwords = [self.inverse_vocab[idx] for idx in token_ids]
        return "".join(subwords)

