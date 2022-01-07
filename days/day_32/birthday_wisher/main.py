import datetime
import smtplib
import random
import csv

EMAIL_TEMPLATES = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

EMAIL = "c.antonmeryl.123@gmail.com"
PASSWORD = "Almond123"

TODAY = datetime.datetime.now()


def get_birthdays():
    """
    Read the birthdays.csv and return a dictionary
    """
    with open(file="birthdays.csv", mode="r") as data_file:
        birthdays = csv.reader(data_file)
        birthdays_dictionary = {item[0]: {
            "email": item[1],
            "month": int(item[3]),
            "day": int(item[4])
        } for item in birthdays if item[0] != "name"}
        return birthdays_dictionary


def get_email_template(name):
    """
    Read a random email template
    """
    with open(file=random.choice(EMAIL_TEMPLATES), mode="r") as email_template:
        template = email_template.read()
        new_letter = template.replace("[NAME]", name.strip())
        return new_letter


def send_email(email, body):
    """
    Send the email
    """
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=email, msg=f"Subject:Happy Birthday\n\n{body}")


def wish_birthday():
    """
    Go through the dictionary of birthdays and send email if there is a matching day
    """
    birthdays = get_birthdays()
    for birthday in birthdays:
        if birthdays[birthday]['day'] == TODAY.day and birthdays[birthday]['month'] == TODAY.month:
            send_email(email=birthdays[birthday]['email'], body=get_email_template(birthday))


wish_birthday()
