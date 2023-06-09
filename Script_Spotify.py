import spotipy
import Creds
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=f"{Creds.spotify_client_id}",
                                               client_secret=f"{Creds.spotify_client_secret}",
                                               redirect_uri=f"{Creds.spotify_redirect_uri}",
                                               scope="user-library-read"))
print("We log in")
# Saved song to favorite
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
