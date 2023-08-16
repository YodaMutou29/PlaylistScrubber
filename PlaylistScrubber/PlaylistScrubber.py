import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth, CacheFileHandler
import spotipy.util as util

client_id = "c730bca803934d55a8e1506b587c4e28"
client_secret = "2a72499150dd4af2ae472cbb7d8ad63a"
user_id = '5670rl0yy85qry0ae7jkufi5s'
authorization_url = 'https://accounts.spotify.com/authorize'
token_url = 'https://accounts.spotify.com/api/token'
redirect_uri ='http://localhost:8080/'
scope = ['playlist-modify-private',
         'playlist-read-private']
cache_path = r"C:\Users\jenna\PlaylistScrubber\cache"

sp_oauth = SpotifyOAuth(client_id=client_id,
                    client_secret=client_secret,
                    redirect_uri=redirect_uri,
                    scope=scope,
                    cache_handler=CacheFileHandler(cache_path=cache_path))

# Get user access token
sp = spotipy.Spotify(auth_manager=sp_oauth)

'''
def AuthorizeOAuth():
    sp_oauth = SpotifyOAuth(client_id=client_id,
                    client_secret=client_secret,
                    redirect_uri=redirect_uri,
                    scope=scope,
                    cache_handler=CacheFileHandler(cache_path=cache_path))

    # Get user access token
    return spotipy.Spotify(auth_manager=sp_oauth)

sp = AuthorizeOAuth()
'''


class PlaylistScrubber:
    def AuthorizeClient(self):
        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


    def GetTracksFromPlaylistID(playlist_id, spotify=None) :

        if spotify:
            sp = spotify
            #sp = AuthorizeOAuth()

        track_names = []
        offset = 0

        while len(track_names) % 100 == 0:
            playlist_items = sp.playlist_items(playlist_id,
                                            fields="items(track(name))",
                                            offset=offset,
                                            additional_types=['track'])
            if not playlist_items:
                break

            offset += 100
            for item in playlist_items["items"]:
                if item["track"]["name"]:
                    track_names.append(item["track"]["name"])

                print(track_names[-1])

        return sorted(track_names)
'''
playlistUrl = input("Enter a playlist url:")
for track in PlaylistScrubber.GetTracksFromPlaylistUrl(playlistUrl):
    print(track)
'''