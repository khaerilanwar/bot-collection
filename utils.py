from art import text2art
from termcolor import colored
from datetime import datetime

def banner(word, color, background=None):
    ascii_art = text2art(word)
    color_art = colored(ascii_art, color=color, on_color=background)
    print(color_art)

def opening():
    banner("Facebook", "light_red")
    today = datetime.now()
    print(colored(today.strftime('%A, %d %B %Y'), "light_green").center(62))
    print(53 * "-")

    # About Author
    print(colored("Author\t  : Khaeril Anwar", "light_blue"))
    print(colored("Telegram  : https://t.me/khaerilanwr", "light_blue"))
    print(colored("Github\t  : https://github.com/khaerilanwar", "light_blue"))
    print(colored("Youtube\t  : https://www.youtube.com/@khaerilanwarr", "light_blue"))
    print(53 * "-")