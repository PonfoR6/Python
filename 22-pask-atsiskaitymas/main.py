from tkinter import *
import random
import pyperclip
from tkinter import messagebox
import json


def random_password():
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    symbols = list('!@#$%^&*()_+')
    letters_lower = list(map(str.lower, letters))
    letters.extend(letters_lower)

    num_letters = random.randint(8, 10)
    num_numbers = random.randint(1, 2)
    num_symbols = random.randint(1, 2)

    random_letters = [random.choice(letters)
                      for i in range(num_letters)]
    random_numbers = [random.choice(numbers)
                      for i in range(num_numbers)]
    random_symbols = [random.choice(symbols)
                      for i in range(num_symbols)]

    created_password = random_letters + random_numbers + random_symbols

    random.shuffle(created_password)
    created_password = ''.join(created_password)

    password_entry.delete(0, END)
    password_entry.insert(0, created_password)

    pyperclip.copy(created_password)


def save_pass():
    user_website = web_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()

    new_data = {
        user_website: {
            'email': user_email,
            'password': user_password
        }
    }
    if len(user_website) != 0 and len(user_password) != 0 and len(user_email) != 0:

        try:
            with open("pass.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("pass.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            is_correct = messagebox.askyesno(
                title=f"{user_website}",
                message=f"\n'email': {user_email}\n'password': {user_password}\n\nAre you sure?")
            if is_correct:
                with open("pass.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                    web_entry.delete(0, END)
                    password_entry.delete(0, END)
    else:
        messagebox.showwarning(
            title="Error",
            message="All fields must be filled."
        )


def website_name():
    user_website = web_entry.get()
    try:
        with open("pass.json", "r") as data_file:
            data = json.load(data_file)
            user_password = data[user_website]["password"]
            user_email = data[user_website]["email"]
            password_entry.delete(0, END)
            password_entry.insert(0, user_password)
            email_entry.delete(0, END)
            email_entry.insert(0, user_email)
    except KeyError as error_msg:
        messagebox.showinfo(title="Key Error", message=f"website {error_msg} has no password")
    except FileNotFoundError as error_msg:
        messagebox.showinfo(message="Password does not exist.")


def login():
    window2 = Tk()
    window2.title("Main page")
    window2.geometry("100x100")

    logged_in = Label(window2, text=" hi:) ")
    logged_in.pack()


# def encrypt_word():
#     text = encryption_entry.get()
#     s = 4
#     result = ""
#     for i in range(len(text)):
#         char = text[i]
#     if char.isupper():
#         result += chr((ord(char) + s - 65) % 26 + 65)
#     else:
#         result += chr((ord(char) + s - 97) % 26 + 97)
#
#     encryption_entry.delete(0, END)
#     encryption_entry.insert(0, result)

def encrypt():
    result = ""
    text = encryption_entry.get()
    s = 4

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    encryption_entry.delete(0, END)
    encryption_entry.insert(0, result)


window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=50)

lbl_web = Label(text='Website:')
lbl_web.grid(row=1, column=0, sticky="W")

web_entry = Entry(font=("Roboto", 15))
web_entry.grid(row=1, column=1, columnspan=2, sticky="EW")

lbl_email = Label(text="Email:")
lbl_email.grid(row=2, column=0, sticky="W")

password_entry = Entry(font=("Roboto", 15))
password_entry.grid(row=3, column=1, sticky="EW")

web_name = Button(text="Search", command=website_name)
web_name.grid(row=1, column=2, sticky="EW")

email_entry = Entry(font=("Roboto", 15))
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "email@gmail.com")

btn_save = Button(text="Add", command=save_pass)
btn_save.grid(row=4, column=1, columnspan=2, sticky="EW")
btn_save.config(pady=2)

lbl_password = Label(text="Password:")
lbl_password.grid(row=3, column=0, sticky="W")

gen_password = Button(text="Generate Password", command=random_password)
gen_password.grid(row=3, column=2, sticky="EW")

login_button = Button(text="Login", command=login)
login_button.grid(row=5, column=1, columnspan=2, sticky="EW")

encryption_entry = Entry(font=("Roboto", 15))
encryption_entry.grid(row=6, column=1, columnspan=2, sticky="EW")

encryption_btn = Button(text="Encrypt word", command=encrypt)
encryption_btn.grid(row=6, column=2, columnspan=2, sticky="W")

window.mainloop()
