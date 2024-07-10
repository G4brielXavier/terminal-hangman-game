from colorama import Fore, Back

def help_text_formatter(msg):
    print(Fore.GREEN + '//' + Fore.WHITE + 'Help: ' + msg)
    
def line_formatter():
    print()
    print(Fore.CYAN + '-'*50)
    print(Back.RESET)
    
def spaces_formatter(qty):
    for _ in range(qty):
        print()
