def find_repeats(counter):
    repeats = []
    for key, count in counter.items():
        if count > 1:
            repeats.append(key)
    return repeats

def value_counts(word):
    counter = {}
    for char in word:
        counter[char] = counter.get(char,0) + 1
    return counter

print(find_repeats(value_counts('investigator')))