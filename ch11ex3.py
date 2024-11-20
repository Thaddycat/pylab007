letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range( len( letters ) )
letter_map = dict( zip( letters, numbers ) )

def shift_word(word, shift):
    ciphtertext = ''
    for l in word:
        l_index = (letter_map[l] + shift) % len(letters)
        ciphtertext += letters[l_index]
    return ciphtertext


if __name__ == '__main__':
    print(shift_word('cheer', 7))
    print(shift_word('melon', 16))