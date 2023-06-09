import pylast
import Creds

password_hash = pylast.md5(f"{Creds.lastfm_password}")

network = pylast.LastFMNetwork(
    api_key=f"{Creds.lastfm_api_key}",
    api_secret=f"{Creds.lastfm_api_secret}",
    username=f"{Creds.lastfm_username}",
    password_hash=password_hash,
)

# Now you can use that object everywhere
# track = network.get_track("Iron Maiden", "The Nomad")
# track.love()
# track.add_tags(("awesome", "favorite"))