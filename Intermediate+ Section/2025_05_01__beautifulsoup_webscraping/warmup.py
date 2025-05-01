from bs4 import BeautifulSoup
import requests
"""
Get to know BeautifulSoup
"""
with open('website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headers = soup.select(selector=".heading")
print(headers)

"""
Use BeautifulSoup on a live website
"""
response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.find(name="a").get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_upvote_index = article_upvotes.index(max(article_upvotes))
print(article_texts[max_upvote_index])
print(article_links[max_upvote_index])
