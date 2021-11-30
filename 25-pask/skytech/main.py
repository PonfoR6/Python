from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.skytech.lt/"
DRIVER_PATH = r"C:\Users\Admin\Desktop\chromedriver\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)

register_btn = driver.find_element(By.CLASS_NAME, "link-register")
register_btn.click()

# name_input = driver.find_element(By.XPATH, '//*[@id="checkout_login_register"]/div[1]/div[2]/input')
# surname_input = driver.find_element(By.NAME, "pavarde")
# phone_input = driver.find_element(By.NAME, "phone")
# mail_input = driver.find_element(By.NAME, "mail")
# pass_input = driver.find_element(By.NAME, "pass")
# pass2_input = driver.find_element(By.NAME, "pass2")
#
# name_input.send_keys("Qwerty")
# surname_input.send_keys("qwerty")
# phone_input.send_keys("9999")
# mail_input.send_keys("qwe@qwe.com")
# pass_input.send_keys("password")
# pass2_input.send_keys("password")
