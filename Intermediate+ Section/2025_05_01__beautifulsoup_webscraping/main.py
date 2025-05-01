"""
Project Descriotion:
1. Scrape the top 100 movies of all time from a website. Generate a text file called movies.txt that lists the movie titles in ascending order (starting from 1).
   The result should look something like this:
    1) The Godfather
    2) The Empire Strikes Back
    3) The Dark Knight
    4) The Shawshank Redemption
    ...
   The idea behind this project is to be able to use BeautifulSoup to obtain some data - like movie titles - from a website like Empire's (or from, say Timeout or
   Stacker that have curated similar lists). Make sure to use the archive's URL as websites can change often.

Completed: 5/1/2025
"""
import requests
from bs4 import BeautifulSoup
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

movie_list = [item.getText() for item in soup.find_all(name="h3", class_="title")]
movie_list.reverse()

with open("movies.txt", "w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")
