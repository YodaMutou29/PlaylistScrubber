# PlaylistScrubber
Allows you to scrub a Spotify playlist clean of any list of words.

This will be done using the spotipy API to get all track titles in a
playlist, then use a separate API to get lyrics from song titles.
The words to exclude from the playlist will be input via command line.
