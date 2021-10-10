import csv
import random
import pandas
from datetime import datetime
import smtplib

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_condition = str(monday.condition)
MY_EMAIL = "testspm55@gmail.com"
PASSWORD = ""

letter_number = random.randint(1, 3)
data = pandas.read_csv("birthdays.csv")
db_year = int(data.year)
db_month = int(data.month)
db_day = int(data.day)
# db_year = 1997
# db_month = 08
# db_day = 16
birthday = db_year, db_month, db_day

if birthday == datetime.today().date():
    f = open(f"letter_{letter_number}", "r")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="kryo2005@gmail.com",
            msg=f"Subject:Happy Birthday!\n\n{f}"
        )




