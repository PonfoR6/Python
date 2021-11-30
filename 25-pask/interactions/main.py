from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

URL = "https://www.skytech.lt/"
DRIVER_PATH = r"C:\Users\Admin\Desktop\chromedriver\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)

query_field = driver.find_element(By.NAME, "q")
query_field.send_keys("for")
query_field.send_keys(Keys.ENTER)

titles = driver.find_elements(By.CSS_SELECTOR, "ul.list-recent-events li h3")

for title in titles:
    print(title.text)