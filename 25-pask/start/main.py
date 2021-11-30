from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"
DRIVER_PATH = r"C:\Users\Admin\Desktop\chromedriver\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)

introduction = driver.find_element(By.CSS_SELECTOR, ".introduction p")

print(introduction.text)

survey_btn = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/span[2]/a')
print(survey_btn.text)
survey_btn.click()

driver.switch_to.window(driver.window_handles[1])

agreement = driver.find_element(By.XPATH, '//*[@id="sgE-6564873-1-255-box"]/div/ul/li/label')
agreement.click()