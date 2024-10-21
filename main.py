# Top 100 songs Spotify playlist
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Step 1: Get date from the user from which we want the top 100 songs from
print("Spotify Playlist Creator!")
year = input("Please enter the year in YYYY format (e.g. 2000): ")
print(f"Your playlist will comprise of top 100 songs from Pitchfork for the year {year}")


# Step 2: Request web page data from Pitchfork for top 100 songs for the input date
PITCHFORK_URL = f"https://pitchfork.com/features/lists-and-guides/best-songs-{year}/"

response = requests.get(url=PITCHFORK_URL)
response.raise_for_status()
pitchfork_page = response.text


# Step 3: Create a soup and extract 100 songs using selectors
soup = BeautifulSoup(pitchfork_page, "lxml")

top_100_songs = soup.select(selector=".body__inner-container h2")
top_100_songs = [song.getText() for song in top_100_songs]

# ----- Process songs list further ----- #
print(top_100_songs)

# Step 4: Authenticate Spotify
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_path="token.txt"))

user_id = sp.current_user()["id"]

# Step 5: Create song URIs to add it in spotify
song_uris = []
for song in top_100_songs:
    song_name = song.split(": ")[1]
    song_name = song_name[1:-1]
    result = sp.search(q=f"track:{song_name} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song_name} doesn't exist in Spotify. Skipped.")

print(f"Total songs found: {len(song_uris)}")


# Step 6: Create a new user playlist
playlist = sp.user_playlist_create(user=user_id,
                                   name=f"Pitchfork {year} Top 100 songs",
                                   public=False,
                                   description="This playlist is created using a Python script!")

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"Pitchfork top songs from {year} was added successfully to the Spotify Playlist!")
