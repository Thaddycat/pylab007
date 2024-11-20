def value_counts(word):
    counter = {}
    for char in word:
        counter[char] = counter.get(char,0) + 1
    return counter

print(value_counts('abracadabra'))