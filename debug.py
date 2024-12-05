# print(f"{5*"-"} Isi Data Berikut! {5*"-"}")
# email = input(f"{5 * " "} Email Facebook\t: ")
# password = input(f"{5 * " "} Password Facebook\t: ")

from utils import banner
from termcolor import colored
from datetime import datetime

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

# Menerima inputan data
print(colored("Isi Data Berikut!", "light_yellow").center(62))
email = input(colored("Email Facebook\t     : ", "light_yellow"))
password = input(colored("Kata Sandi Facebook  : ", "light_yellow"))
id_grup = input(colored("ID Grup Facebook     : ", "light_yellow"))
id_admin = input(colored("ID Admin Grup\t     : ", "light_yellow"))
komentar = input(colored("Komentar\t     : ", "light_yellow"))

# import sys
# import time

# # Karakter spinner
# spinner = ['|', '/', '-', '\\']

# # Simulasi proses dengan spinner
# for _ in range(20):
#     for char in spinner:
#         sys.stdout.write(f'\r{char} Loading...')
#         sys.stdout.flush()
#         time.sleep(0.1)
#     print(_)

# print("\nDone!")
# print(56 * "-")