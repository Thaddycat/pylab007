from itertools import filterfalse


def has_duplicates(word):
    counter = {}
    for char in word:
        counter[char] = counter.get(char, 0) + 1
    for count in counter.values():
        if count > 1:
            return True
    return False

print(has_duplicates('uncopyrightable'))