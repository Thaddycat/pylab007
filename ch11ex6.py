def word_distance(word1, word2):
    return sum(1 for c1, c2 in zip(word1, word2) if c1 != c2)

def word_distance_indexes(word1, word2):
    return [i for i, pair in enumerate(zip(word1, word2)) if pair[0] != pair[1]]


if __name__ == '__main__':
    print(word_distance('hello', 'hxllo'))
    print(word_distance('ample', 'apply'))
    print(word_distance('kitten', 'mutton'))
    print(word_distance_indexes('hello', 'halpo'))
    
word1 = "apple"
word2 = "auble"
distance = word_distance(word1, word2)
print(f'The word distance between "{word1}" and "{word2}" is: {distance}')