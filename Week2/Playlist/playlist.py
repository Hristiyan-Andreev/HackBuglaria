from song import Song


class Playlist:

    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)
