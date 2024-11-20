import json
from os.path import exists

def get_key(word):
    return ''.join(sorted(word.strip()))

def save_sorted_dict(word_dict, file_path):
    with open(file_path, 'w') as wd_file:
        json.dump(word_dict, wd_file, indent=True)

def word_distance(word1, word2):
    return sum(1 for c1, c2 in zip(word1, word2) if c1 != c2)

def load_sorted_dict(file_path):
    word_dict = {}
    with open(file_path, 'r') as word_file:
        for word in word_file:
            key = get_key( word )
            key_list = word_dict.get( key, [] )
            key_list.append( word.strip() )
            word_dict[key] = key_list
    return word_dict

def load_word_dict(file_path, words_path='words.txt'):
    word_dict = {}
    if not exists(file_path):
        word_dict = load_sorted_dict(words_path)
        save_sorted_dict(word_dict, file_path)
    else:
        with open(file_path, 'r') as wd_file:
            word_dict = json.load(wd_file)
    return word_dict

if __name__ == '__main__':
    word_dict_path = 'dict.json'
    words_path = 'words.txt'
    word_dict = load_word_dict(word_dict_path, words_path)
    for k, v in word_dict.items():
        if len(v) > 1:  # These are all the words that have anagrams
            for i in range( len( v ) ): # Start with the first word
                for j in range( i + 1, len( v ) ): # Compare it to each word but not to itself
                    if word_distance( v[i], v[j] ) == 2:
                        print( f'Metathesis: {v[i]} and {v[j]}' )