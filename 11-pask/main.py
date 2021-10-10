import smtplib

MY_EMAIL = "testspm55@gmail.com"
PASSWORD = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="kryo2005@gmail.com",
        msg="Subject:Hello from python\n\nHello this is python code!"
    )