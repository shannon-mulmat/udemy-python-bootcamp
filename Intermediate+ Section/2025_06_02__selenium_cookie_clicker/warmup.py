from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1")
driver.get("https://python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is: ${price_dollar}.{price_cents}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# doc_lnk = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_lnk.text)
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)

# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
"""
# Wikipedia walkthrough
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# article_count.click()

# Find element by link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input? by Name
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)
"""

"""
# Fake form fill-out and click
driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Shannon")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Mulmat")

email = driver.find_element(By.NAME, value="email")
email.send_keys("shan_mul@gmail.com")

signup_button = driver.find_element(By.CSS_SELECTOR, value="form button")
signup_button.click()
"""
