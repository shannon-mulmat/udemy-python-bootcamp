"""
Project Description:
- Write a program that scapes a copy of a Zillow site using BeautifulSoup, then uses Selenium to
  auto-fill and submit a Google Form for each property with the property's address, price, and link

Completed: 6/18/2025
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
ZILLOW_URL = 'https://appbrewery.github.io/Zillow-Clone/'
GOOGLE_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSflXUEi1KCy2tJ1rHzxhypGVC4rd2ng_7cOHQ88wNYWGgaapA/viewform?usp=dialog'

header = {
    "User-Agent": "Chrome/84.0.4147.125",
    "Accept-Language": "en-US"
}

response = requests.get(ZILLOW_URL, headers=header)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

link_list = [item.get("href") for item in soup.find_all(class_='property-card-link')]
price_list = [item.getText().replace('+', '').replace('/mo', '').replace(' 1bd', '').replace(' 1 bd', '') for item in soup.find_all(class_='PropertyCardWrapper__StyledPriceLine')]
address_list = [item.getText().strip().replace(' |', ',') for item in soup.find_all(name='address')]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(link_list)):
    driver.get(GOOGLE_FORM)
    time.sleep(2)

    address_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    price_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    link_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    submit_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'

    address_box = driver.find_element(By.XPATH, value=address_xpath)
    price_box = driver.find_element(By.XPATH, value=price_xpath)
    link_box = driver.find_element(By.XPATH, value=link_xpath)
    submit_button = driver.find_element(By.XPATH, value=submit_button_xpath)

    address_box.send_keys(address_list[n])
    price_box.send_keys(price_list[n])
    link_box.send_keys(link_list[n])
    submit_button.click()
