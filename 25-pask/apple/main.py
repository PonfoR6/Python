from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from tkinter import *

window = Tk()
window.title("Choose Date")
window.geometry("500x500")

day_entry = Entry(font=("Roboto", 10))
day_entry.grid(column=1, row=1, sticky="EW")

month_entry = Entry(font=("Roboto", 10))
month_entry.grid(column=1, row=2, sticky="EW")

year_entry = Entry(font=("Roboto", 10))
year_entry.grid(column=1, row=3, sticky="EW")

# URL = "https://www.officialcharts.com/charts/uk-top-40-singles-chart/"
# DRIVER_PATH = r"C:\Users\Admin\Desktop\chromedriver\chromedriver_win32\chromedriver.exe"
#
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver.get(URL)
#
# agree_btn = driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
# agree_btn.click()
#
# select_day = Select(driver.find_element(By.XPATH, '//*[@id="main"]/article/div/div[1]/div[1]/nav/div/div/div/div/div[2]/select'))
# select_day.select_by_visible_text(f'{day}')
#
# select_month = Select(driver.find_element(By.XPATH, '//*[@id="main"]/article/div/div[1]/div[1]/nav/div/div/div/div/div[3]/select'))
# select_month.select_by_visible_text(f'{month}')
#
# select_year = Select(driver.find_element(By.XPATH, '//*[@id="main"]/article/div/div[1]/div[1]/nav/div/div/div/div/div[4]/select'))
# select_year.select_by_visible_text(f'{year}')
#
# go_btn = driver.find_element(By.XPATH, '//*[@id="main"]/article/div/div[1]/div[1]/nav/div/div/div/div/input')
# go_btn.click()

window.mainloop()
