from art import text2art
from termcolor import colored
from datetime import datetime

def pilihan_menu():
    pilihan = input(colored(f"{6* " "}Pilihan : ", "light_green"))
    return pilihan

def banner(word, color, background=None):
    ascii_art = text2art(word)
    color_art = colored(ascii_art, color=color, on_color=background)
    print(color_art)

def menu():
    print(colored(53*"-", "light_magenta"))
    print(colored("|", "light_magenta"), colored("Silakan pilih tools dibawah ini!", "light_cyan").center(58), colored("|", "light_magenta"))
    print(colored(53*"-", "light_magenta"))
    print(colored("[ 1 ]", "light_yellow"), colored("Auto Post Feed", "light_green"), )
    print(colored("[ 2 ]", "light_yellow"), colored("Auto Post Group", "light_green"))
    print(colored("[ 3 ]", "light_yellow"), colored("Auto Like Post", "light_green"))
    print(colored("[ 4 ]", "light_yellow"), colored("Spam Comment Post Group", "light_green"))
    print(colored("[ 5 ]", "light_yellow"), colored("Spam Comment Post Feed", "light_green"))
    print(colored("[ 6 ]", "light_yellow"), colored("Fast Comment New Post Group", "light_green"))
    print(colored(f"{6* " "}{47*"-"}", "light_magenta"))

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
    menu()
