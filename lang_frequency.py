from collections import Counter
import re
import sys


SPLIT_LIST = ['\.', ',', ':', ';', '\(', '\)', '!', '\?', '"', '«', '»']
SPLIT_PATTERN = '\s|' + '|'.join('\s?{}\s?'.format(punctuation) for punctuation in SPLIT_LIST)


def main():
    try:
        get_most_frequent_words(sys.argv[1])
    except IndexError:
        print(
            'Please, call the script with a path to a TXT file. '
            'You need to specify the path as the first script argument.'
        )


def get_most_frequent_words(filepath):
    frequency_dict = Counter(list(load_words(filepath)))
    for word in frequency_dict.most_common(10):
        print(word[0])


def load_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            for word in re.split(SPLIT_PATTERN, line.strip().lower()):
                if word:
                    yield word


if __name__ == '__main__':
    main()
