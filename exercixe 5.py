def add_counters(counter1, counter2):
    total_counter = dict(counter1)
    for key, value in counter2.items():
        total_counter[key] = total_counter.get(key, 0) + value
    return total_counter

def value_counts(word):
    counter = {}
    for char in word:
        counter[char] = counter.get(char,0) + 1
    return counter

counter1 = value_counts('mississippi')
counter2 = value_counts('california')

print(add_counters(counter1, counter2))