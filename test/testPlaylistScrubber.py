from unittest import TestCase

import spotipy 
sp = spotipy.Spotify() 
from spotipy.oauth2 import SpotifyClientCredentials 
import spotipy.util as util

class TestPlaylist(TestCase):
    def __init__(self):
        self.cid = 
        self.secret = "2a72499150dd4af2ae472cbb7d8ad63a"
        self.client_credentials_manager = SpotifyClientCredentials(client_id=self.cid, client_secret=self.secret)
        self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
        testPlaylist = 

    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)

    def test_get_tracks_from_playlist_url(self):
        