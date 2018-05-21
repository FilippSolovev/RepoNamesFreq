from nltk import pos_tag


def check_word_type(word, assumption='verb'):
    word_types = {'verb': {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'},
                  'noun': {'NN', 'NNP', 'NNS'}}
    if not word:
        return False
    pos_info = pos_tag([word])
    return True if pos_info[0][1] in word_types[assumption] else False


def parse_snake_case(sc_name):
    words = sc_name.split('_')
    return [''.join(filter(str.isalpha, word)) for word in words if word]


def extract_words_from_text(sc_string, type_of_word='verb'):
    words = parse_snake_case(sc_string)
    return [word for word in words
            if check_word_type(word, assumption=type_of_word)]
