import nltk
import matplotlib.pyplot as plt

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from collections import Counter

from common import get_all_review_texts

STOP_WORDS = stopwords.words("english") + [".", ",", "!", "?", "'s", "...", "(", ")", "n't", "``", "also", "even", "would", "us", "could", "one", "'ve", "-", "''", "'m"]
print("STOP_WORDS are:")
print(STOP_WORDS)


def stem_text(text):
    porter = PorterStemmer()
    tokens = nltk.word_tokenize(text)
    tokens_stemmed = []

    for token in tokens:
        tokens_stemmed.append(porter.stem(token))
    return " ".join(tokens_stemmed)


if __name__ == "__main__":
    texts = get_all_review_texts()
    texts_stemmed = [stem_text(text) for text in texts]
    porter = PorterStemmer()

    len2num = Counter()
    len2num_stemmed = Counter()
    word2freq = Counter()
    word2freq_stemmed = Counter()

    for text in texts:
        tokens = nltk.word_tokenize(text)
        len2num[len(tokens)] += 1
        for token in tokens:
            unified_token = token.lower()
            if unified_token not in STOP_WORDS:
                word2freq[unified_token] += 1

    for text in texts_stemmed:
        tokens = nltk.word_tokenize(text)
        len2num_stemmed[len(tokens)] += 1
        for token in tokens:
            unified_token = token.lower()
            if unified_token not in STOP_WORDS:
                word2freq_stemmed[unified_token] += 1

    lens, nums = zip(*sorted(len2num.items()))
    lens_stemmed, nums_stemmed = zip(*sorted(len2num_stemmed.items()))

    plt.bar(lens, nums, label="Without Stemming")
    plt.legend()
    plt.xlabel("Length of Review")
    plt.ylabel("No. of Reviews")
    plt.title("Distribution of Review Lengths (without Stemming)")
    plt.savefig("assets/task3-fig1-dist-nostem")
    # plt.show()
    plt.clf()

    plt.bar(lens_stemmed, nums_stemmed, label="With Stemming")
    plt.legend()
    plt.xlabel("Length of Review")
    plt.ylabel("No. of Reviews")
    plt.title("Distribution of Review Lengths (without Stemming)")
    plt.savefig("assets/task3-fig2-dist-withstem")
    # plt.show()

    print("Without Stemming")
    print("\tMax Review Length: {}".format(max(lens)))  # 1194
    print("\tLength {} has a maximum number of reviews: {}".format(nums.index(max(nums)), max(nums)))  # 30, 132
    print("\tTop 20 frequent words: {}".format(word2freq.most_common(20)))

    print("With Stemming")
    print("\tMax Review Length: {}".format(max(lens_stemmed)))  # 1194
    print("\tLength {} has a maximum number of reviews: {}".format(nums_stemmed.index(max(nums_stemmed)), max(nums_stemmed)))
    # 30, 133 (slightly different from 132 due to syntax error of reviews e.g. " ., ")
    print("\tTop 20 frequent words: {}".format(word2freq_stemmed.most_common(20)))


