import smtplib
import random
from datetime import datetime
# import datetime as dt

MY_EMAIL = "testspm55@gmail.com"
PASSWORD = ""
random_lines = random.choice(open("quotes.txt").readlines())

if datetime.today().isoweekday() == 7:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="kryo2005@gmail.com",
            msg=f"Subject:Monday quote\n\n{random_lines}"
        )


# MY_EMAIL = "testspm55@gmail.com"
# PASSWORD = ""
# now = dt.datetime.now()
# weekday = now.weekday()
#
# if weekday == 6:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs="kryo2005@gmail.com",
#             msg=f"Subject:Monday motivation\n\n{quote}"
#         )
