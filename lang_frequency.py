import argparse
from collections import Counter
import os
import string


def _main():
    parser = argparse.ArgumentParser()
    args = get_args(parser)
    if not os.path.exists(args.path):
        parser.error(
            'file with text not found, '
            'specify existing path in `path` argument'
        )
    words = split_to_words(load_text(args.path))

    for word, _ in get_most_common_words(words, args.count):
        print(word)


def get_args(parser):
    parser.add_argument(
        'path',
        help='Path to file with text to analyze'
    )
    parser.add_argument(
        '-c',
        '--count',
        metavar='count',
        help='The number of most common words to display',
        type=int,
        default=10
    )
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
