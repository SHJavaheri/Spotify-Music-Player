from spotipy.oauth2 import SpotifyOAuth
import spotipy

client_id = '4dca3ddfc10249ebb3c149dd8362f964'
client_secret = '3d4e9bc438aa4a8185d9746e0ac4c6f9'
redirect_uri = 'http://localhost:8888/callback'

# Asking the authenticator manager to authenticate the variables we fed it
auth_manager = SpotifyOAuth(client_id = client_id,
                            client_secret = client_secret,
                            redirect_uri = redirect_uri,
                            scope = 'user-read-playback-state user-read-currently-playing user-modify-playback-state')

sp = spotipy.Spotify(auth_manager = auth_manager)

current_playback = sp.current_playback()

# Setting items retrieved from Spotify as variables/placeholders
track_name = current_playback['item']['name']
artists = current_playback['item']['artists']
artist_names = [artist['name'] for artist in artists]
artist_names_str = ', '.join(artist_names)
album_name = current_playback['item']['album']['name']
duration_ms = current_playback['item']['duration_ms']

# Converting duration of song from milliseconds to minutes and seconds
minutes = duration_ms // 60000
seconds = (duration_ms % 60000) // 1000
duration_str = f"{minutes}:{seconds}"

print(f"Track: {track_name}")
print(f"Artists: {artist_names_str}")
print(f"Album: {album_name}")
print(f"Duration: {duration_str}")
