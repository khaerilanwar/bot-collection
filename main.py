from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# Menerima inputan email dan sandi facebook
email = input("Masukkan email\t: ")
password = input("Masukkan password\t: ")

driver.quit()