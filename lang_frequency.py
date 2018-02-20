import argparse
from collections import Counter
import string

MOST_COMMON_COUNT = 10


def _main():
    args = get_args()
    words = split_to_words(load_text(args.filename))

    for word, _ in get_most_common_words(words, MOST_COMMON_COUNT):
        print(word)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Path to TXT file with text to analyze')
    return parser.parse_args()


def load_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            yield line


def split_to_words(text):
    for line in text:
        for word in line.split(' '):
            word = clean_word(word)
            if word.isalpha():
                yield word


def clean_word(word):
    return word.lower().strip('{punctuation}{whitespace}«»'.format(
        punctuation=string.punctuation,
        whitespace=string.whitespace
    ))


def get_most_common_words(words, most_common_count):
    frequencies = Counter(words)
    return frequencies.most_common(most_common_count)


if __name__ == '__main__':
    _main()
