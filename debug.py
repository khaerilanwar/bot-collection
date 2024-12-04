# print(f"{5*"-"} Isi Data Berikut! {5*"-"}")
# email = input(f"{5 * " "} Email Facebook\t: ")
# password = input(f"{5 * " "} Password Facebook\t: ")

from utils import banner
from termcolor import colored
from datetime import datetime
from locale import setlocale, LC_TIME

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

# Menerima inputan data
print(colored("Isi Data Berikut!", "light_yellow").center(80))
email = input(colored("Email Facebook\t\t: ", "light_yellow"))
password = input(colored("Kata Sandi Facebook\t: ", "light_yellow"))
link_group = input(colored("Link Grup Facebook\t: ", "light_yellow"))
nama_admin = input(colored("Nama Admin Grup\t\t: ", "light_yellow"))

import sys
import time

# Karakter spinner
spinner = ['|', '/', '-', '\\']

# Simulasi proses dengan spinner
for _ in range(20):
    for char in spinner:
        sys.stdout.write(f'\r{char} Loading...')
        sys.stdout.flush()
        time.sleep(0.1)
    print(_)

print("\nDone!")
print(74 * "-")