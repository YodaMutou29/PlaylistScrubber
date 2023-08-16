import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth, CacheFileHandler
import spotipy.util as util

# setting up authorization
client_id = "c730bca803934d55a8e1506b587c4e28" # Client ID
client_secret = "2a72499150dd4af2ae472cbb7d8ad63a" # Client Secret
# saving the info you're going to need
username = '5670rl0yy85qry0ae7jkufi5s' # Account Number
#scope = 'user-library-read' #check the documentation
authorization_url = 'https://accounts.spotify.com/authorize'
token_url = 'https://accounts.spotify.com/api/token'
redirect_uri ='https://localhost.com/callback/'

'''
#token = util.prompt_for_user_token(username,scope,client_id='client_id_number',client_secret='client_secret',redirect_uri='https://localhost.com/callback/')
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
'''
scope = ['playlist-modify-private', 'playlist-read-private', 'playlist-read-public']
sp_oauth = SpotifyOAuth(client_id=client_id,
                        client_secret=client_secret,
                        redirect_uri="http://localhost:8080/",
                        scope=scope,
                        cache_handler=CacheFileHandler(cache_path=r"C:\Users\jenna\PlaylistScrubber\cache"))

# Get user access token
sp = spotipy.Spotify(auth_manager=sp_oauth)

class PlaylistScrubber:
    def GetTracksFromPlaylistID(playlist_id) :
        trackNames = []

        for item in sp.playlist_items(playlist_id, fields="items(track(name))", offset=100, additional_types=['track']):
            if item["name"]:
                trackNames.append(item["name"])

            print(trackNames[-1])

        return sorted(trackNames)
'''
playlistUrl = input("Enter a playlist url:")
for track in PlaylistScrubber.GetTracksFromPlaylistUrl(playlistUrl):
    print(track)
'''