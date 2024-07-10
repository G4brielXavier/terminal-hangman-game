# Hangman Game
# version: HG-02a
# release day: 2024/07/08 - Monday

from funcs import *
from Dotket.dotket import *

animals_base = ['dog', 'cat', 'habbit', 'rhino', 'cow', 'monkey', 'elephant', 'bee', 'frog', 'lion', 'pig', 'ounce', 'raccoon', 'leopard', 'ant', 'salamander', 'mouse', 'goat', 'ox', 'locust']
objects_base = ['pen', 'paper', 'book', 'pencil', 'computer', 'monitor', 'keyboard', 'eraser', 'ink', 'ball', 'scissor', 'rock', 'plant', 'tree', 'magic cube', 'key', 'phone', 'cloth', 'shirt', 'pants', 't-shirts']

letter = '' # variavel que recebe a letra para adivinhar
attemps = 0 # variavel que controla o numero de tentativas

head = '' # variavel que armazena a "head" do hangman
left_body_right = '' # variavel que armazena o braço esquerdo e direito e o corpo
left_foot_right = '' # variavel que armazena a perna esquerda e a direita

letters_used = [] # Lista de letras usadas

spaces_formatter(2)
DOTKET_hi(True)
sleep(1)
DOTKET_speak(False, 'Welcome to ' + Fore.GREEN + '</Hangman Game>')
sleep(1)
spaces_formatter(2)

theme = set_theme(animals_base, objects_base) # o tema escolhido é retornado para a variavel

# Condição que verifica se o tema foi escolhido
if not theme is None:
    
    word = chosse_word(theme) # Variavel que armazena a palavra escolhida dentro do tema selecionado
    word_line = create_word_lines(word) # Variavel que armazena a palavra escolhida em forma de linhas
    word_correct = ['' for _ in range(len(word_line))] # Variavel que armazena as letras em sua posição correta
    
    DOTKET_happy(True, 'The word was choiced.')
    print(Fore.WHITE)
    
    # Enquanto a palavra de adivinhação não é igual a palavra escolhida e as tentativas forem menores que 7
    while not str(word_correct) == word or attemps < 7:
        
        build_character(letters_used, word_line, head, left_body_right, left_foot_right) #Esta função ira criar a estrutura da forca
        letter = ask() # Esta variavel vai armazenar a letra que o usuario for escolher
        
        if not len(letters_used) == 0:
            for i in range(len(letters_used)):
                if letter == letters_used[i]:
                    DOTKET_speak(True, 'This letter was used.')
                    pass
                else:
                    letters_used.append(letter) # Armazenando a letra escolhida dentro da lista de letras usadas
                    # Passar por uma range do tamanho da lista de linhas
                    for n in range(0, len(word_line) - 1):
                        # Verifica se uma das letras usadas não é igual a letra escolhida ou se a lista de letras usadas esta vazia
                        if len(letters_used) == 0: 
                            # Verifica se cada letra da palavra escolhida não é igual a de adivinhação 
                            if not list(word)[n] == letter:
                                attemps += 1 # Aumenta mais nas tentativas
                                
                                # e verifica a condição para montar o hangman
                                if attemps == 1:
                                    head = 'o'
                                elif attemps == 2:
                                    left_body_right = '|'
                                elif attemps == 3:
                                    left_body_right = '||'
                                elif attemps == 4:
                                    left_body_right = '|||'
                                elif attemps == 5:
                                    left_foot_right = 'L'
                                elif attemps == 6:
                                    left_foot_right = 'LL'
                            else:
                                w_tolist = list(word) # Converte a string da palavra para uma lista
                                word_line[w_tolist.index(letter)] = letter # Na posição que estiver a letra correta na palavra correta convertida para lista, pegando este index e colocando lista de linhas, no colocamos que para que seja igual a letra escolhida
                                word_correct[word_line.index(letter)] = letter # Na posição que estiver a letra correta na palavra correta convertida para lista, pegando este index e colocando lista de linhas, no colocamos que para que seja igual a letra escolhida
                            
                            # Se o numero de tentativas chegar em 7, fim de jogo 
                            if attemps == 7:
                                DOTKET_error(True, f'Attemps Limit, The word was "{word}"')
                                break
                        # Se for igual continua o while 
                        else:
                            spaces_formatter(2)
                            pass
                    else:
                        pass    
else:
    DOTKET_speak(True, 'Bye or run again.')
    spaces_formatter(2)
