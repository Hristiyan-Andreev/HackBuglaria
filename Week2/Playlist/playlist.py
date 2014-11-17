from song import Song


class Playlist:

    def __init__(self):
        self.playlist = {}

    def add_song(self, song):
        if song.artist not in self.playlist:
            self.playlist[song.artist] = {}
        self.playlist[song.artist][song.title] = Song()
        self.playlist[song.artist][song.title].album = song.album
        self.playlist[song.artist][song.title].rating = song.rating
        self.playlist[song.artist][song.title].length = song.length
        self.playlist[song.artist][song.title].bitrate = song.bitrate

    #def remove_song(self, songName):

