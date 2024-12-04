import sys, time, threading
from utils import opening
from selenium import webdriver
from termcolor import colored
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Karakter spinner
spinner = ['|', '/', '-', '\\']

# Fungsi untuk menampilkan spinner
def show_spinner():
    while not done:
        for char in spinner:
            sys.stdout.write(f'\r{char} Loading...')
            sys.stdout.flush()
            time.sleep(0.1)

opening()

# Menerima inputan data
print(colored("Isi Data Berikut!", "light_yellow").center(80))
email = input(colored("Email Facebook\t\t: ", "light_yellow"))
password = input(colored("Kata Sandi Facebook\t: ", "light_yellow"))
id_grup = input(colored("ID Grup Facebook\t: ", "light_yellow"))
id_admin = input(colored("ID Admin Grup\t\t: ", "light_yellow"))
komentar = input(colored("Komentar\t\t: ", "light_yellow"))

#  Status spinner
done = False

# Spinner berjalan di thread terpisah
spinner_thread = threading.Thread(target=show_spinner)
spinner_thread.start()

try:
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    # LOGIN KE AKUN FACEBOOK
    driver.get("https://web.facebook.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email'))).send_keys(email)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'pass'))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'login'))).click()
    time.sleep(5)

    # Memulai melakukan komentar
    link_post_grup_user = f"https://web.facebook.com/groups/{id_grup}/user/{id_admin}"
    driver.get(link_post_grup_user)
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Beri komentar"][role="button"]'))).click()
    
    input_comment = driver.switch_to.active_element
    input_comment.send_keys(komentar)
    input_comment.send_keys(Keys.ENTER)
    
    # Hentikan spinner dan hapus loading
    done = True
    spinner_thread.join()
    sys.stdout.write('\r' + ' ' * 20 + '\r')  # Menghapus baris loading
    sys.stdout.flush()

    print("Berhasil melakukan komentar!")

except Exception as e:
    print(colored(f"Error: {e}", "red"))

driver.quit()