"""
Project Description:
1. Use https://www.alphavantage.co
    - When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
2. Use https://newsapi.org
    - Instead of printing ("Get News"), get the first 3 news pieces for the COMPANY_NAME.
3. Send yourself an email with the percentage change and each article's title and description.

Completed: 3/31/2025
"""
import requests
import smtplib
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCKS_URL = "https://www.alphavantage.co/query"
STOCKS_API_KEY = "PT11BEBWJPVQ53AI"
NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "7f630784827648d5b09cc0391b8083ef"
GMAIL_EMAIL = "smpythonproject@gmail.com"
GMAIL_APP_PASSWORD = "yarxbvegquzkuxiw"
YAHOO_EMAIL = "smpythonproject@yahoo.com"

def percent_diff(new_value, old_value):
    try:
        p_diff = ((new_value - old_value) / old_value) * 100
        if p_diff < 0:
            delta = "DOWN"
        elif p_diff > 0:
            delta = "UP"
        else:
            delta = "NEUTRAL"
    except ZeroDivisionError:
        p_diff = 0
        delta = 0
    return abs(p_diff), delta

stocks_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCKS_API_KEY
}
response = requests.get(url=STOCKS_URL, params=stocks_parameters)
response.raise_for_status()
stocks_data = response.json()["Time Series (Daily)"]

key_list = list(stocks_data.keys())

yesterday_close_price = float(stocks_data[key_list[0]]["4. close"])
day_before_yesterday_close_price = float(stocks_data[key_list[1]]["4. close"])

p_diff, delta = percent_diff(yesterday_close_price, day_before_yesterday_close_price)

if p_diff >= 5:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }
    response = requests.get(url=NEWS_URL, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()

    first_3_articles = news_data["articles"][:3]
    art_1_title = first_3_articles[0]["title"].encode("utf-8")
    art_1_desc = first_3_articles[0]["description"].encode("utf-8")
    art_2_title = first_3_articles[1]["title"].encode("utf-8")
    art_2_desc = first_3_articles[1]["description"].encode("utf-8")
    art_3_title = first_3_articles[2]["title"].encode("utf-8")
    art_3_desc = first_3_articles[2]["description"].encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=GMAIL_EMAIL, password=GMAIL_APP_PASSWORD)
        connection.sendmail(
            from_addr=GMAIL_EMAIL,
            to_addrs=YAHOO_EMAIL,
            msg=f"Subject:Tesla Stock Price Changed Over 5%\n\n"
                f"{STOCK}: {delta} {round(p_diff, 2)}%\n\n"
                f"Headline 1: {art_1_title}\nBrief 1: {art_1_desc}\n\n"
                f"Headline 2: {art_2_title}\nBrief 2: {art_2_desc}\n\n"
                f"Headline 3: {art_3_title}\nBrief 3: {art_3_desc}"
        )
