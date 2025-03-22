"""
Topics Covered:
1. SMTP - sending emails via Python
2. Datetime module

Project Description:
- Create a program that automatically sends Happy Birthday emails to friends and family on their birthday
  1. Update the birthdays.csv
  2. Check if today matches a birthday in the birthdays.csv
  3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
  4. Send the letter generated in step 3 to that person's email address.

Completed: 3/21/2025
"""
import smtplib
import datetime as dt
import random
import csv
import pandas as pd
from my_birthdays import my_birthdays

GMAIL_EMAIL = "smpythonproject@gmail.com"
GMAIL_APP_PASSWORD = "yarxbvegquzkuxiw"
YAHOO_EMAIL = "smpythonproject@yahoo.com"

existing_birthdays = set()

try:
    with open("birthdays.csv", "r") as birthday_file:
        reader = csv.reader(birthday_file)
        for row in reader:
            existing_birthdays.add(tuple(row))
except FileNotFoundError:
    with open("birthdays.csv", "w") as birthday_file:
        writer = csv.writer(birthday_file)
        for row in my_birthdays:
            writer.writerow(row)
else:
    with open("birthdays.csv", "a") as birthday_file:
        writer = csv.writer(birthday_file)
        for row in my_birthdays:
            row_as_strings = tuple(map(str, row))
            if row_as_strings not in existing_birthdays:
                writer.writerow(row_as_strings)

today_tuple = (dt.datetime.now().month, dt.datetime.now().day)
bday_df = pd.read_csv("birthdays.csv")
bday_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in bday_df.iterrows()}

if today_tuple in bday_dict:
    bday_person = bday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        bday_email = contents.replace("[NAME]", bday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=GMAIL_EMAIL, password=GMAIL_APP_PASSWORD)
        connection.sendmail(
            from_addr=GMAIL_EMAIL,
            to_addrs=bday_person["email"],
            msg=f"Subject:Happy Birthday, {bday_person['name']}!\n\n{bday_email}"
        )
