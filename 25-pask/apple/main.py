from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from tkinter import *
from tkinter import messagebox
import time

URL = "https://www.officialcharts.com/charts/uk-top-40-singles-chart/"
DRIVER_PATH = r"C:\Users\user\OneDrive\Desktop\driver(programing)\chromedriver.exe"


def search_web():
    if len(day_entry.get()) != 0 and len(month_entry.get()) != 0 and len(year_entry.get()) != 0:
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.get(URL)

        agree_btn = driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
        agree_btn.click()

        select_day = Select(driver.find_element(By.XPATH,
                                                '//*[@id="main"]/article/div/div[1]/div[1]/nav/div/div/div/div/div[2]/select'))
        select_day.select_by_visible_text(f'{day_entry.get()}')

        select_month = Select(driver.find_element(By.XPATH,
                                                  '//*[@id="main"]/article/div/div[1]/div[1]/nav/div/div/div/div/div[3]/select'))
        select_month.select_by_visible_text(f'{month_entry.get()}')

        select_year = Select(driver.find_element(By.XPATH,
                                                 '//*[@id="main"]/article/div/div[1]/div[1]/nav/div/div/div/div/div[4]/select'))
        select_year.select_by_visible_text(f'{year_entry.get()}')

        go_btn = driver.find_element(By.XPATH, '//*[@id="main"]/article/div/div[1]/div[1]/nav/div/div/div/div/input')
        go_btn.click()
        time.sleep(100)
    else:
        messagebox.showerror("Error", "All fields must be filled")


window = Tk()
window.title("Billboard Search")
window.geometry("400x200")
window.config(bg='#f399a3')

day_entry = Entry(font=("Roboto", 15), bg='#f3aabf')
day_entry.grid(column=2, row=1, columnspan=2, sticky="EW")

month_entry = Entry(font=("Roboto", 15), bg='#f3aabf')
month_entry.grid(column=2, row=2, columnspan=2, sticky="EW")

year_entry = Entry(font=("Roboto", 15), bg='#f3aabf')
year_entry.grid(column=2, row=3, columnspan=2, sticky="EW")

year_lbl = Label(text="Enter year:", bg='#f399a3')
year_lbl.grid(column=0, row=3, sticky="W")

month_lbl = Label(text="Enter month(short):", bg='#f399a3')
month_lbl.grid(column=0, row=2, sticky="W")

day_lbl = Label(text="Enter day:", bg='#f399a3')
day_lbl.grid(column=0, row=1, sticky="W")

search_btn = Button(text="Search", command=search_web, bg='#f3aabf')
search_btn.grid(column=2, row=4, columnspan=2, sticky="EW")

window.mainloop()
