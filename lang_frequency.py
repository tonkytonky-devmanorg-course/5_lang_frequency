import argparse
from collections import Counter
import string

MOST_COMMON_COUNT = 10


def _main():
    args = get_args()
    words = proceed_word(load_words(args.filename))

    for word, _ in get_most_common_words(words, MOST_COMMON_COUNT):
        print(word)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Path to TXT file with text to analyze')
    return parser.parse_args()


def load_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            for word in line.split(' '):
                yield word


def proceed_word(words):
    for word in words:
        word = word.lower().strip(string.punctuation + string.whitespace + '«»')
        if word:
            yield word


def get_most_common_words(words, most_common_count):
    frequencies = Counter(words)
    return frequencies.most_common(most_common_count)


if __name__ == '__main__':
    _main()
