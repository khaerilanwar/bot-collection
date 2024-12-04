import os, time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

email_fb = os.getenv('EMAIL_FB')
password_fb = os.getenv('PASSWORD_FB')
link_login = os.getenv('LINK_LOGIN')
link_group = os.getenv('LINK_GROUP')

# Options Chrome Browser
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--headless=new")

# Instance WebDriver Chrome
driver = webdriver.Chrome("driver\chromedriver.exe", options=options)

# LOGIN KE AKUN  FACEBOOK
driver.get(link_login)
input_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
input_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'pass')))
button_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'login')))
input_email.send_keys(email_fb)
time.sleep(3)
input_password.send_keys(password_fb)
time.sleep(3)
button_login.click()

time.sleep(5)

driver.get(link_group)
time.sleep(3)

# SCROLL HALAMAN GROUP FACEBOOK
end_time = time.time() + 2
body = driver.find_element(By.TAG_NAME, 'body')
while time.time() < end_time:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    
time.sleep(3)

# MENGAMBIL SEMUA POSTINGAN
feed = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')
feed_posts = feed.find_elements(By.XPATH, './div')

for post in feed_posts:
    try:
        # Mencari postingan dengan orang tertentu
        profile_name = post.find_element(By.CSS_SELECTOR, 'div[data-ad-rendering-role="profile_name"]').text
        print(profile_name)

        # Tombol komentar postingan
        # button_comment = post.find_element(By.CSS_SELECTOR, 'div[aria-label="Beri komentar"][role="button"]')
        # button_comment.click()

        # Berpindah ke input komentar yang aktif
        # input_comment = driver.switch_to.active_element
        # input_comment.send_keys("Jasa CV Online Terbaik")
        # input_comment.send_keys(Keys.SHIFT, Keys.ENTER)
        # input_comment.send_keys("WhatsApp : 0821 3763 3527")
        # input_comment.send_keys(Keys.ENTER)

        print("Komentar berhasil dikirim!")

        # time.sleep(30)
    except:
        continue

driver.quit()
print("Program berhasil dijalankan")