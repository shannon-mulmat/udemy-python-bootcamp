"""
Project Description:
- Create a program that scapes the Billboard Top 100 songs list for a date entered by the user, and creates a Spotify playlist of those songs

Completed: 5/2/2025
"""
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
BASE_URL =  "https://www.billboard.com/charts/hot-100/"
SPOTIFY_CLIENT_ID = '1220c10d758e4da5bc7eb3cbef85688f'
SPOTIFY_CLIENT_SECRET = 'aa17c47b924e4984b729541e5385ba56'

# Spotify authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://open.spotify.com/",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# Scraping Billboard 100
musical_date = input("What date do you want to travel to? Enter in the format YYYY-MM-DD: ")
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
response = requests.get(url=f'{BASE_URL}{musical_date}/', headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
song_names = [item.getText().strip() for item in soup.select("li ul li h3")]

# Searching Spotify for songs by title
song_uris = []
year = musical_date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{musical_date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
