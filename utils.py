from art import text2art
from termcolor import colored

def banner(word, color, background=None):
    ascii_art = text2art(word)
    color_art = colored(ascii_art, color=color, on_color=background)
    print(color_art)