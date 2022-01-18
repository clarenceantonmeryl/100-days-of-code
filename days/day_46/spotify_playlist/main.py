import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "b057df4715bd4e4fa888ae6040925ca6"
CLIENT_SECRET = "57ae12b4e3f749b4bdaade29a3b9bea7"

day = "2007-11-28"

titles = []
artists = []
spotify_uris = []

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{day}/")
response.raise_for_status()
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
songs = soup.find_all("div", class_="o-chart-results-list-row-container")

for song in songs:
    song_li_1 = song.find(name='li', class_="lrv-u-width-100p")
    song_li_2 = song_li_1.find(name='li', class_="o-chart-results-list__item")
    song_h3 = song_li_2.find(name='h3', id="title-of-a-story")
    song_name = song_h3.text.strip()
    song_artist = song_li_2.find(name='span', class_="c-label").text.strip()
    titles.append(song_name)
    artists.append(song_artist)

print(titles)

auth_manager = SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://127.0.0.1:5500/",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    show_dialog=True,
    cache_path="token.txt"
)

sp = spotipy.Spotify(
    auth_manager=auth_manager
)

user_id = sp.current_user()["id"]

print(user_id)

year = int(day.split('-')[0])

for song in titles:

    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        song_uri = result["tracks"]["items"][0]["uri"]
        spotify_uris.append(song_uri)
    except IndexError:
        print(f"{song} does not exist.")
    else:
        print(song_uri, song)

print("URIs", spotify_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"Top {len(spotify_uris)} songs on {day}", public=False)
print(playlist)

playlist_id = playlist['id']

print("Playlist ID", playlist_id)

sp.playlist_add_items(playlist_id=playlist_id, items=spotify_uris)