import numpy as np
import string


def convert(code):
    bin_code = bin(code)[2:].zfill(6)[::-1]
    return [[int(bin_code[j + i * 3]) for i in range(2)] for j in range(3)]


LETTERS_NUMBERS = list(map(convert,
                           [1, 3, 9, 25, 17, 11, 27, 19, 10, 26,
                            5, 7, 13, 29, 21, 15, 31, 23, 14, 30,
                            37, 39, 62, 45, 61, 53, 47, 63, 55, 46, 26]))
CAPITAL_FORMAT = convert(32)
NUMBER_FORMAT = convert(60)
PUNCTUATION = {",": convert(2), "-": convert(18), "?": convert(38),
               "!": convert(22), ".": convert(50), "_": convert(36)}
WHITESPACE = convert(0)


def add_symbol(symbol):
# Returns braille representation of a symbol
    if symbol.isalpha():                                                                    
        pos = string.ascii_lowercase.index(symbol.lower())
        # Position of a letter in alphabet (starts with 0 and corresponds with LETTERS_NUMBERS index)
        if symbol.isupper():
        # Add column of zeros after every symbol
            return np.hstack((np.array((CAPITAL_FORMAT)), np.zeros((3,1), dtype='int'), \
                   np.array((LETTERS_NUMBERS[pos])), np.zeros((3,1), dtype='int')))
        return np.hstack((np.array((LETTERS_NUMBERS[pos])), np.zeros((3,1), dtype='int')))

    elif symbol.isdigit():
        pos = 9 if symbol == '0' else int(symbol) - 1
        # Position of a number in LETTERS_NUMBERS
        return np.hstack((np.array((NUMBER_FORMAT)), np.zeros((3,1), dtype='int'), \
               np.array((LETTERS_NUMBERS[pos])), np.zeros((3,1), dtype='int')))

    elif symbol in PUNCTUATION:
        return np.hstack((np.array((PUNCTUATION[symbol])), np.zeros((3,1), dtype='int')))

    else:
        return np.hstack((np.array((WHITESPACE)), np.zeros((3,1), dtype='int')))

        
def split_array(arr):                                                                                   
# Splits NumPy array so that each part contains no more than 10 symbols and returns a list of NumPy arrays
    split = []
    if arr.shape[1] <= 29:
        split.append(arr)
        return split 
    while True:
        a, b = np.array_split(arr, [29], axis=1)
        b = b[:, 1:]
        # Remove excess zeros column from the beginning of the second part
        split.append(a)       
        if b.shape[1] <= 29:
            split.append(b)
            return split
        arr = b


def braille_page(text: str):
    braille = np.array([], dtype='int').reshape((3,0))
    # Create empty array with 3 rows to enable appending to it
    for ch in text:
        braille = np.append(braille, add_symbol(ch), axis=1)
        # Fill array with braille symbols
    braille = braille[:, :-1]
    # Remove excess zeros column(from add_symbol) from the end of the array
    split = split_array(braille)
    if len(split) > 1:                                                                                     
        split[-1] = np.append(split[-1], np.zeros((3, 29 - split[-1].shape[1]), dtype='int'), axis=1)
        # If more than one line, fill the rest of the last line with zeros to equalize the page
        for i in range(1, len(split)):
            split[0] = np.vstack((split[0], np.zeros((1, 29), dtype='int'), split[i]))
            # Add row of zeros after each line
    return split[0].tolist()          
    #Convert NumPy array to list of lists
