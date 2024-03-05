import spotipy
from spotipy.oauth2 import SpotifyOAuth
from song_list import SearchSong

client_id = "ae2ac5bb80f346d7a01034ab1e407394"
client_secret = "2b4e70e4fedd4539b3f58f3c48506176"
redirect_uri = "http://example.com"
username = "5horbob0aomu3e8mfc6l5e4xj"

# Authorization
scope = "playlist-modify-private playlist-modify-public"
auth_manager = SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
my_bot = spotipy.Spotify(auth_manager=auth_manager)

# Scraping Billboard 100
search_date = input("what year you would like to travel to in YYYY-MM-DD format.: ")
print("Searching top 100 song...........")
search_song = SearchSong(date=search_date)
top_100_song = search_song.song_list
print(search_song.url)


print("Searching song on spotify.............")
song_uris = []
year = search_date.split("-")[0]
for song in top_100_song:
    result = my_bot.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create a playlist
playlist_name = f"{search_date} Billboard "
playlist = my_bot.user_playlist_create(username, playlist_name, public=True)

# Adding songs found into the new playlist
my_bot.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# Save the playlist URL
playlist_url = playlist['external_urls']['spotify']
print(f"\nPlaylist URL: {playlist_url}")
