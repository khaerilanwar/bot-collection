from art import text2art
from termcolor import colored
from datetime import datetime
from locale import setlocale, LC_TIME

def banner(word, color, background=None):
    ascii_art = text2art(word)
    color_art = colored(ascii_art, color=color, on_color=background)
    print(color_art)

def opening():
    banner("Bot Facebook", "light_red")
    # Menampilkan tanggal sekarang pakai bahasa Indonesia
    setlocale(LC_TIME, "id_ID")
    today = datetime.now()
    print(colored(today.strftime('%A, %d %B %Y'), "light_green").center(80))
    print(74 * "-")

    # About Author
    print(colored("Author\t\t: Khaeril Anwar", "light_blue"))
    print(colored("Telegram\t: https://t.me/khaerilanwr", "light_blue"))
    print(colored("Github\t\t: https://github.com/khaerilanwar", "light_blue"))
    print(colored("Youtube\t\t: https://www.youtube.com/@khaerilanwarr", "light_blue"))
    print(74 * "-")