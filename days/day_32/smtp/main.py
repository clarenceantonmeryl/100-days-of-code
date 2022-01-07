import smtplib
import datetime
import random

my_email = "c.antonmeryl.123@gmail.com"
password = "Almond123"

with open(file="quotes.txt", mode="r") as quote_file:
    quotes = quote_file.readlines()

print(quotes)

now = datetime.datetime.now()

if now.weekday() == 4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            to_addrs=my_email,
            from_addr=my_email,
            msg=f"Subject:Quote\n\n{random.choice(quotes)}"
        )

#
# print(now.microsecond)
# print(now.weekday())
# date_of_birth = datetime.datetime(year=2007, month=11, day=28, hour=15, second=15, minute=18)
# print(date_of_birth)

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="anton_meryl@yahoo.co.in",
#         msg="Subject:Hello\n\nHello world"
#     )
