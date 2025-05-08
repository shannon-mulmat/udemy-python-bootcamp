"""
Project Description:
- Create a program that emails you when the price for an item on Amazon drops below a certain amount

Completed: 5/8/2025
"""
from bs4 import BeautifulSoup
import requests
import smtplib
URL = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
GMAIL_EMAIL = "smpythonproject@gmail.com"
GMAIL_APP_PASSWORD = ""
YAHOO_EMAIL = "smpythonproject@yahoo.com"
THRESHOLD_PRICE = float(100)

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

response = requests.get(url=URL, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
current_price = float(soup.find(class_='aok-offscreen').getText().split("$")[1])
product_title = soup.find(id="productTitle").getText().strip().encode("utf-8")

if current_price < THRESHOLD_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=GMAIL_EMAIL, password=GMAIL_APP_PASSWORD)
        connection.sendmail(
            from_addr=GMAIL_EMAIL,
            to_addrs=YAHOO_EMAIL,
            msg=f"Subject: Alert!! Price Drop on Your Item!!\n\n"
                f"The item you are watching has dropped below your price threshold of ${THRESHOLD_PRICE} to ${current_price}!\n\n"
                f"{product_title}\n\n"
                f"Click here to view your item: {URL}"
        )
