from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from bs4 import BeautifulSoup


URL = "https://www.google.com"
DRIVER_PATH = r"C:\Users\Admin\Desktop\driver\chromedriver.exe"

answer = input("What topic would you like to look for?")

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)

agree = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div')
agree.click()

query = f'{answer}'
links = []
n_pages = 5
for page in range(1, n_pages):
    url = "http://www.google.com/search?q=" + query + "&start=" +      str((page - 1) * 10)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    search = soup.find_all('div', class_="yuRUbf")
    for h in search:
        links.append(h.a.get('href'))

print(links)
