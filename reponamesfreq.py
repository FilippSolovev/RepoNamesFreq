import argparse

from astparser import fetch_list_of_node_names
from wordfinder import extract_words_from_text
from words import Words
from repohandler import clone_repo

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')


def flatter_a_list(list_of_lists):
    output = []
    for sublist in list_of_lists:
        for item in sublist:
            output.append(item)
    return output


def get_words_within_path(path, type_of_node='function', type_of_word='verb'):
    list_of_nodes = fetch_list_of_node_names(path, type_of_node=type_of_node)

    words = []

    for word in list_of_nodes:
        words.append(extract_words_from_text(
            word,
            type_of_word=type_of_word))

    words = flatter_a_list(words)

    logger.info(f'total {len(words)} words, {len(set(words))} unique')

    return Words(words)


if __name__ == '__main__':

    TOP_SIZE = 10

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", type=str)
    parser.add_argument("-s", "--source", type=str)
    parser.add_argument("-wt", "--wordtype", type=str)
    parser.add_argument("-o", "--output", type=str)
    args = parser.parse_args()

    path = '.'
    if args.url:
        url = args.url
        path = clone_repo(url).working_tree_dir

    type_of_node = 'function'
    if args.source:
        if args.source.lower() == 'var':
            type_of_node = 'variable'

    type_of_word = 'verb'
    if args.wordtype:
        if args.wordtype.lower() == 'noun':
            type_of_word = 'noun'

    words = get_words_within_path(path, type_of_node=type_of_node,
                                  type_of_word=type_of_word)

    if args.output:
        if args.output.lower() == 'json':
            words.to_json()
        elif args.output.lower() == 'csv':
            words.to_csv()
    else:
        words.print_most_common(head=TOP_SIZE)
