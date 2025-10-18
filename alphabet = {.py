# block_alphabet.py
# ASCII block letters in "██" style, large size only, better spacing for visibility

letters = {
    "A": [
        "   ██   ",
        "  █  █  ",
        "  █  █  ",
        "  ████  ",
        "  █  █  ",
        "  █  █  ",
        "        "
    ],
    "B": [
        " ████  ",
        " █   █ ",
        " ████  ",
        " █   █ ",
        " █   █ ",
        " ████  ",
        "       "
    ],
    "C": [
        "  ████ ",
        " █     ",
        " █     ",
        " █     ",
        " █     ",
        "  ████ ",
        "       "
    ],
    "D": [
        " ████  ",
        " █   █ ",
        " █   █ ",
        " █   █ ",
        " █   █ ",
        " ████  ",
        "       "
    ],
    "E": [
        " █████ ",
        " █     ",
        " ████  ",
        " █     ",
        " █     ",
        " █████ ",
        "       "
    ],
    "F": [
        " █████ ",
        " █     ",
        " ████  ",
        " █     ",
        " █     ",
        " █     ",
        "       "
    ],
    "G": [
        "  ████  ",
        " █      ",
        " █  ██  ",
        " █   █  ",
        " █   █  ",
        "  ████  ",
        "        "
    ],
    "H": [
        " █   █ ",
        " █   █ ",
        " █████ ",
        " █   █ ",
        " █   █ ",
        " █   █ ",
        "       "
    ],
    "I": [
        " █████ ",
        "   █   ",
        "   █   ",
        "   █   ",
        "   █   ",
        " █████ ",
        "       "
    ],
    "J": [
        "   ███ ",
        "     █ ",
        "     █ ",
        "     █ ",
        " █   █ ",
        "  ███  ",
        "       "
    ],
    "K": [
        " █   █ ",
        " █  █  ",
        " ███   ",
        " █  █  ",
        " █   █ ",
        " █    █",
        "       "
    ],
    "L": [
        " █     ",
        " █     ",
        " █     ",
        " █     ",
        " █     ",
        " █████ ",
        "       "
    ],
    "M": [
        " █   █ ",
        " ██ ██ ",
        " █ █ █ ",
        " █   █ ",
        " █   █ ",
        " █   █ ",
        "       "
    ],
    "N": [
        " █   █ ",
        " ██  █ ",
        " █ █ █ ",
        " █  ██ ",
        " █   █ ",
        " █   █ ",
        "       "
    ],
    "O": [
        "  ███  ",
        " █   █ ",
        " █   █ ",
        " █   █ ",
        " █   █ ",
        "  ███  ",
        "       "
    ],
    "P": [
        " ████  ",
        " █   █ ",
        " ████  ",
        " █     ",
        " █     ",
        " █     ",
        "       "
    ],
    "Q": [
        "  ████  ",
        " █    █ ",
        " █    █ ",
        " █    █ ",
        " █    █ ",
        "  ████  ",
        "        "
    ],
    "R": [
        " ████  ",
        " █   █ ",
        " ████  ",
        " █  █  ",
        " █   █ ",
        " █    █",
        "       "
    ],
    "S": [
        "  ████ ",
        " █     ",
        "  ███  ",
        "     █ ",
        "     █ ",
        " ████  ",
        "       "
    ],
    "T": [
        " █████ ",
        "   █   ",
        "   █   ",
        "   █   ",
        "   █   ",
        "   █   ",
        "       "
    ],
    "U": [
        " █   █ ",
        " █   █ ",
        " █   █ ",
        " █   █ ",
        " █   █ ",
        "  ███  ",
        "       "
    ],
    "V": [
        " █   █ ",
        " █   █ ",
        " █   █ ",
        "  █ █  ",
        "  █ █  ",
        "   █   ",
        "       "
    ],
    "W": [
        " █   █ ",
        " █   █ ",
        " █ █ █ ",
        " █ █ █ ",
        " ██ ██ ",
        " █   █ ",
        "       "
    ],
    "X": [
        " █   █ ",
        "  █ █  ",
        "   █   ",
        "   █   ",
        "  █ █  ",
        " █   █ ",
        "       "
    ],
    "Y": [
        " █   █ ",
        "  █ █  ",
        "   █   ",
        "   █   ",
        "   █   ",
        "   █   ",
        "       "
    ],
    "Z": [
        " █████ ",
        "    █  ",
        "   █   ",
        "  █    ",
        " █     ",
        " █████ ",
        "       "
    ]
}




def print_word(word, orientation='horizontal'):
    """
    Prints a word in ASCII block letters.
    
    Args:
        word (str): The word to print (A-Z).
        orientation (str): 'horizontal' or 'vertical'.
    """
    word = word.upper()
    
    if orientation == 'horizontal':
        # Determine the height of letters (all same in this set)
        letter_height = len(next(iter(letters.values())))
        lines = ['' for _ in range(letter_height)]
        
        for ch in word:
            if ch in letters:
                for i in range(letter_height):
                    lines[i] += letters[ch][i] + '  '  # 2 spaces between letters
            else:
                for i in range(letter_height):
                    lines[i] += ' ' * len(letters['A'][i]) + '  '
        
        # Print all lines
        for line in lines:
            print(line)

    elif orientation == 'vertical':
        for ch in word:
            if ch in letters:
                for row in letters[ch]:
                    print(row)
                print()  # blank line between letters
            else:
                for _ in range(len(letters['A'])):
                    print(' ' * len(letters['A'][0]))
                print()
    else:
        print("Invalid orientation. Use 'horizontal' or 'vertical'.")

# --- Example usage ---
print("Horizontal format:")
print_word('HELLO', 'horizontal')

print("\nVertical format:")
print_word('HELLO', 'vertical')