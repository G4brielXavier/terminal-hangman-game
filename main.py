# Hangman Game
# version: HG-02a
# release day: 2024/07/08 - Monday

from funcs import *
from Dotket.dotket import *

animals_base = ['dog', 'cat', 'habbit', 'rhino', 'cow', 'monkey', 'elephant', 'bee', 'frog', 'lion', 'pig', 'ounce', 'raccoon', 'leopard', 'ant', 'salamander', 'mouse', 'goat', 'ox', 'locust']
objects_base = ['pen', 'paper', 'book', 'pencil', 'computer', 'monitor', 'keyboard', 'eraser', 'ink', 'ball', 'scissor', 'rock', 'plant', 'tree', 'magic cube', 'key', 'phone', 'cloth', 'shirt', 'pants', 't-shirts']

DOTKET_hi(True)
sleep(1)
DOTKET_speak(False, 'Welcome to ' + Fore.GREEN + '</Hangman Game>')
sleep(1)
spaces_formatter(2)
theme = set_theme(animals_base, objects_base)

word_guess = ''
attemps = 0

head = ''
left_body_right = ''
left_foot_right = ''

if not theme is None:
    word = chosse_word(theme)
    word_line = create_word_lines(word)
    DOTKET_happy(True, 'The word was choiced.')
    print(Fore.WHITE)
    
    while not word_guess == word or attemps < 7:
        build_character(word_line, head, left_body_right, left_foot_right)
        letter = ask()
        create_structure(word)
        
        if not word_guess == word:
            attemps += 1
            
            if attemps == 1:
                head = 'o'
            elif attemps == 2:
                left_body_right = '|'
            elif attemps == 3:
                left_body_right = '||'
            elif attemps == 4:
                left_body_right = '|||'
            elif attemps == 5:
                left_foot_right = '|'
            elif attemps == 6:
                left_foot_right = '||'
                
        if attemps == 7:
            DOTKET_error(True, f'Attemps Limit, The word was "{word}"')
            break 
else:
    DOTKET_speak(True, 'Bye or run again.')
