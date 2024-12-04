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
# link_group = os.getenv('LINK_GROUP')

# Options Chrome Browser
options = webdriver.ChromeOptions()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--headless=new")

# Instance WebDriver Chrome
driver = webdriver.Chrome(options=options)

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

# BUKA HALAMAN GROUP POSTINGAN ORANG
# link_group = f"https://web.facebook.com/groups/888792567828940/user/100054607266052"
link_group = f"https://web.facebook.com/groups/888792567828940/user/61555512613274"

driver.get(link_group)
time.sleep(3)

# body = driver.find_element(By.TAG_NAME, 'body')
# body.send_keys(Keys.PAGE_DOWN)
# time.sleep(3)

start_posts = driver.find_elements(By.CSS_SELECTOR, '.x1yztbdb.x1n2onr6.xh8yej3.x1ja2u2z')
isi_last_post = start_posts[0].find_element(By.CSS_SELECTOR, 'div[data-ad-rendering-role="story_message"]').text

while True:
    try:
        all_posts = driver.find_elements(By.CSS_SELECTOR, '.x1yztbdb.x1n2onr6.xh8yej3.x1ja2u2z')
        latest_post = all_posts[0]
        content_last_post = latest_post.find_element(By.CSS_SELECTOR, 'div[data-ad-rendering-role="story_message"]').text
        if isi_last_post == content_last_post:
            driver.refresh()
            print("--- Refresh")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.x1yztbdb.x1n2onr6.xh8yej3.x1ja2u2z')))
        else:
            button_comment_first = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Beri komentar"][role="button"]')
            button_comment_first.click()

            input_comment = driver.switch_to.active_element
            input_comment.send_keys("ini test")
            input_comment.send_keys(Keys.ENTER)
            print("Berhasil posting komentar")
            break
    except Exception as e:
        print(e)
        break

driver.quit()
print("Program berhasil dijalankan")