from colorama import Fore
from Dotket.formatters import *

def DOTKET_hi(icon):
    print(Fore.CYAN + ':]' + Fore.WHITE + ' - ' + 'Hi!') if icon is False else print(Fore.CYAN + ':] Dotket' + Fore.WHITE + ' - ' + 'Hi!')
    
def DOTKET_speak(icon, msg):
    print(Fore.CYAN + ':]' + Fore.WHITE + ' - ' + msg) if icon is False else print(Fore.CYAN + ':] Dotket' + Fore.WHITE + ' - ' + msg)
    
def DOTKET_error(icon, msg):
    line_formatter()
    print(Fore.RED + ':[' + Fore.WHITE + ' - ' + msg) if icon is False else print(Fore.RED + ':[ Dotket "Sad"' + Fore.WHITE + ' - ' + msg)
    line_formatter()
    
def DOTKET_happy(icon, msg):
    line_formatter()
    print(Fore.GREEN + ':D' + Fore.WHITE + ' - ' + msg) if icon is False else print(Fore.GREEN + ':D Dotket "Happy"' + Fore.WHITE + ' - ' + msg)
    line_formatter()