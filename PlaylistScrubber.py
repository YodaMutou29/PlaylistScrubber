import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 
import spotipy.util as util

# setting up authorization
cid = "c730bca803934d55a8e1506b587c4e28" # Client ID
secret = "2a72499150dd4af2ae472cbb7d8ad63a" # Client Secret
# saving the info you're going to need
username = '5670rl0yy85qry0ae7jkufi5s' # Account Number
scope = 'user-library-read' #check the documentation
authorization_url = 'https://accounts.spotify.com/authorize'
token_url = 'https://accounts.spotify.com/api/token'
redirect_uri ='https://localhost.com/callback/'

#token = util.prompt_for_user_token(username,scope,client_id='client_id_number',client_secret='client_secret',redirect_uri='https://localhost.com/callback/')
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

class PlaylistScrubber:
    def GetTracksFromPlaylistURI(playlist_uri) :
        #playlist_URI = playlistUrl.split("/")[-1].split("?")[0]
        trackNames = []
        for track in sp.playlist_tracks(playlist_uri)["items"]:
            trackNames.append(track["track"]["name"])

        return sorted(trackNames)
'''
playlistUrl = input("Enter a playlist url:")
for track in PlaylistScrubber.GetTracksFromPlaylistUrl(playlistUrl):
    print(track)
'''