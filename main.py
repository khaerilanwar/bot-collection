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
print(colored("Isi Data Berikut!", "light_yellow").center(62))
email = input(colored("Email Facebook\t     : ", "light_yellow"))
password = input(colored("Kata Sandi Facebook  : ", "light_yellow"))
id_grup = input(colored("ID Grup Facebook     : ", "light_yellow"))
id_admin = input(colored("ID Admin Grup\t     : ", "light_yellow"))
komentar = input(colored("Komentar\t     : ", "light_yellow"))

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

    link_post_grup_user = f"https://web.facebook.com/groups/{id_grup}/user/{id_admin}"
    driver.get(link_post_grup_user)
    time.sleep(3)   

    postingan_terakhir = driver.find_elements(By.CSS_SELECTOR, '.x1yztbdb.x1n2onr6.xh8yej3.x1ja2u2z')
    isi_post_terakhir = postingan_terakhir[0].find_element(By.CSS_SELECTOR, 'div[data-ad-rendering-role="story_message"]').text if len(postingan_terakhir) > 0 else ""

    # Hentikan spinner dan hapus loading
    done = True
    spinner_thread.join()
    sys.stdout.write('\r' + ' ' * 20 + '\r')  # Menghapus baris loading
    sys.stdout.flush()

    while True:
        try:
            # Jika ada isi postingan terakhir
            if isi_post_terakhir:
                postingan_terbaru = driver.find_elements(By.CSS_SELECTOR, '.x1yztbdb.x1n2onr6.xh8yej3.x1ja2u2z')
                post_terbaru = postingan_terbaru[0]
                isi_post_terbaru = post_terbaru.find_element(By.CSS_SELECTOR, 'div[data-ad-rendering-role="story_message"]').text
                
                if isi_post_terakhir == isi_post_terbaru:
                    driver.refresh()
                    print(colored("-- Refresh", "light_cyan"))
                    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.x1yztbdb.x1n2onr6.xh8yej3.x1ja2u2z')))
                else:
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Beri komentar"][role="button"]'))).click()
                    
                    input_comment = driver.switch_to.active_element
                    input_comment.send_keys(komentar)
                    input_comment.send_keys(Keys.ENTER)

                    print("")
                    print(colored("Komentar Berhasil!", "light_green"))
                    print(colored("Komentar : ", "light_grey"), colored(komentar, "light_green"))
                    print("")

                    break
            
            # Jika tidak ada postingan terakhir
            else:
                postingan_terbaru = driver.find_elements(By.CSS_SELECTOR, '.x1yztbdb.x1n2onr6.xh8yej3.x1ja2u2z')
                if postingan_terbaru:
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Beri komentar"][role="button"]'))).click()
                    
                    input_comment = driver.switch_to.active_element
                    input_comment.send_keys(komentar)
                    input_comment.send_keys(Keys.ENTER)

                    print("")
                    print(colored("Komentar Berhasil!", "light_green"))
                    print(colored("Komentar : ", "light_grey"), colored(komentar, "light_green"))
                    print("")

                    break
                else:
                    driver.refresh()
                    print(colored("-- Refresh", "light_cyan"))
                    # Tunggu hingga halaman selesai dimuat
                    WebDriverWait(driver, 10).until(
                        lambda d: d.execute_script("return document.readyState") == "complete"
                    )

        except Exception as e:
            print(colored(f"Error: {e}", "red"))
            break

    driver.quit()
except Exception as e:
    print(colored(f"Error: {e}", "red"))
