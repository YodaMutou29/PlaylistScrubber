import pytest
from unittest import TestCase
from ..PlaylistScrubber import PlaylistScrubber

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth, CacheFileHandler
import spotipy.util as util

class TestPlaylistScrubber(TestCase):
    def setUp(self):
        self.user_id = "5670rl0yy85qry0ae7jkufi5s"
        self.client_id = "c730bca803934d55a8e1506b587c4e28"
        self.client_secret = "2a72499150dd4af2ae472cbb7d8ad63a"
        scope = ['playlist-modify-private', 'playlist-read-private']
        sp_oauth = SpotifyOAuth(client_id=self.client_id,
                                client_secret=self.client_secret,
                                redirect_uri="http://localhost:8080/",
                                scope=scope,
                                cache_handler=CacheFileHandler(cache_path=r"C:\Users\jenna\PlaylistScrubber\cache"))

        # Get user access token
        self.sp = spotipy.Spotify(auth_manager=sp_oauth)
        self.test_playlist = self.sp.user_playlist_create(user=self.user_id,
                                                          name="Test Playlist",
                                                          public=False)

        tracks = self.sp.artist_top_tracks('spotify:artist:36QJpDe2go2KgaRleHCDTp')
        self.sp.playlist_add_items(playlist_id=self.test_playlist["id"],
                                   items=[track["uri"] for track in tracks["tracks"]])
            
    @pytest.fixture(autouse=True)
    def teardown(self):
        self.sp.current_user_unfollow_playlist(self.test_playlist["id"])

    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)

    def test_get_tracks_from_playlist_url(self):
        track_names = PlaylistScrubber.GetTracksFromPlaylistURI(self.test_playlist["uri"])
        for track in track_names:
            print(track)
        expected_tracks = ["Black Dog - Remaster",
                            "Going to California - Remaster",
                            "Good Times Bad Times - 1993 Remaster",
                            "Immigrant Song - Remaster",
                            "Kashmir - Remaster",
                            "Over the Hills and Far Away - Remaster",
                            "Ramble On - 1990 Remaster",
                            "Rock and Roll - Remaster",
                            "Stairway to Heaven - Remaster",
                            "Whole Lotta Love - 1990 Remaster"]
        self.assertEqual(track_names, expected_tracks)
