def count_value(word):
    counter = {}
    for l in word:
        counter[l] = counter.get(l, 0) + 1
    return counter

def key_func(item):
    return item[1]

def most_frequent_letters(word):
    counter = count_value(word)
    return dict( sorted( counter.items(), key=key_func, reverse=True ) )

if __name__ == '__main__':
    print(most_frequent_letters('hello-world'))