import smtplib
import datetime as dt
import random

GMAIL_EMAIL = "smpythonproject@gmail.com"
GMAIL_APP_PASSWORD = ""
YAHOO_EMAIL = "smpythonproject@yahoo.com"
YAHOO_PASSWORD = ""

today = dt.datetime.now()
day_of_week = today.weekday()

if day_of_week == 4:
    with open("quotes.txt") as quote_file:
        quotes_list = [line.strip("\n") for line in quote_file.readlines()]
        random_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=GMAIL_EMAIL, password=GMAIL_APP_PASSWORD)
        connection.sendmail(
            from_addr=GMAIL_EMAIL,
            to_addrs=YAHOO_EMAIL,
            msg=f"Subject:Happy Friday!\n\n{random_quote}"
        )
