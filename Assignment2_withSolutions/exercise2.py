import collections

def BPE_learner(corpus, num_merges):
    words = [word + "_" for word in corpus.split(" ")]
    vocab = list(set("".join(words)))
    tokens = [list(token) for token in set(words)]
    vocab_count = collections.Counter(words)
    for iteration in range(num_merges):
        counts = {}
        for token in tokens:
            word = "".join(token)
            for t_l, t_r in zip(token[:-1], token[1:]):
                pair = t_l + t_r
                if pair in counts.keys():
                    counts[pair] += vocab_count[word]
                else:
                    counts[pair] = vocab_count[word]
        if len(counts) == 0 or max(counts.values()) == 1:
            print("No more pairings possible")
            break
        else:
            most_common_pair = max(counts, key=counts.get)
            print(f"most common pair: {most_common_pair}")
            vocab.append(most_common_pair)
        for token in tokens:
            ind = 1
            while ind < len(token):
                if token[ind - 1] + token[ind] == most_common_pair:
                    token[ind - 1] = most_common_pair
                    token.pop(ind)
                else:
                    ind += 1
        print(f"new tokens:")
        print(tokens)
        print("--------")
    return vocab


def BPE_tokenizer(text, vocab):
    tokens = list(text.replace(" ", "_"))
    for entry in vocab:
        if len(entry) == 1:
            i = 0
            while i < len(tokens):
                if not tokens[i] in vocab:
                    tokens[i] = "UNK"
                i += 1
        else:
            i = 1
            while i < len(tokens):
                if tokens[i - 1] + tokens[i] == entry:
                    tokens[i - 1] = entry
                    tokens.pop(i)
                i += 1
    return tokens

test_corpus = "low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new"
test_vocab = BPE_learner(test_corpus, 20)
print(test_vocab)
print(BPE_tokenizer(test_corpus, test_vocab))
print(BPE_tokenizer("This is a low test", test_vocab))