def find_anagrams(words):
    anagram_dict = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]


    for anagram_set in anagram_dict.values():
        if len(anagram_set) > 1:
            print(anagram_set)


# Example usage
word_list = [
    'deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled',
    'retainers', 'ternaries', 'generating', 'greatening',
    'resmelts', 'smelters', 'termless', 'hello', 'world'
]

find_anagrams(word_list)