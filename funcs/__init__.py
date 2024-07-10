from colorama import Fore, Back
from random import choice
from time import sleep
#unique import
from Dotket import dotket


def set_theme(animals, objects):
    dotket.DOTKET_speak(True, 'Chosse the theme of game, Animals or Objects.')
    v = input(Fore.GREEN + 'Animals' + Fore.WHITE + ' | ' + Fore.BLUE + 'Objects' + Fore.WHITE + ' : ').lower()
    
    if v in ['animals', 'objects']:
        if v == 'animals':
            return animals
        else:
            return objects
    else:
        dotket.DOTKET_error(True, f'Ops!, This option "{v}" not exist')
        return None

def chosse_word(list):
    return choice(list)

def build_character(l_used, w_line, head, left_body_right, left_foot_right):    
    print(f'Letters Used: {l_used}')
    print()
    print(Fore.WHITE + '______')
    print(Fore.WHITE +'|    |')
    print(Fore.WHITE + f'|    ' + Fore.RED + head)
    print(Fore.WHITE + f'|   ' + Fore.RED + left_body_right)
    print(Fore.WHITE + f'|   ' + Fore.RED + left_foot_right)
    print(Fore.WHITE + '|')
    print(Fore.WHITE + f'| ' + Fore.GREEN + f'{w_line}')
    print()
    
def create_word_lines(word):
    new_word_f = ['_' for _ in range(len(word))]
    return new_word_f

def ask():
    guess_word = input(Fore.WHITE + 'Guess: ')
    return guess_word    

def create_structure(word):
    pass
    # build_character(word_lines, head, left_body_right, left_foot_right)
    
    # if not word_guess == word:
    #     attemps += 1
    # else:
    #     for i in range(len(word)):
    #         if word_guess == word[i]:
    #             word_lines[word.index(word[i])] = i
        
    
        
