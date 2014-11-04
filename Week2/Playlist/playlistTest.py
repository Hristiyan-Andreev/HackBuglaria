from playlist import Playlist
from song import Song
import unittest


class TestPlaylist(unittest.TestCase):

    def test_init_(self):
        playlist1 = Playlist()
        self.assertEqual(playlist1.playlist, [])

    def test_addsong(self):
        song1 = Song("Punta", "Upsurt", "Pop Folk", 5, 3.45, 192)
        #song2 = Song("Kuchko Kosmata", "Upsurt", "Pop Folk", 5, 3.20, 200)
        playlist1 = Playlist()
        playlist1.add_song(song1)
        self.assertTrue(playlist1.playlist[0].title, "Punta")
        self.assertTrue(playlist1.playlist[0].artist, "Uspurt")
        self.assertTrue(playlist1.playlist[0].album, "Pop Folk")
        self.assertTrue(playlist1.playlist[0].rating, 1)
        self.assertTrue(playlist1.playlist[0].length, 3.45)
        self.assertTrue(playlist1.playlist[0].bitrate, 192)


if __name__ == '__main__':
    unittest.main()
