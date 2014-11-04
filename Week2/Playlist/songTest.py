from song import Song
import unittest


class songTest(unittest.TestCase):

    def setUp(self):
        self.song = Song("Punta", "Upsurt", "Pop Folk", 5, 3.45, 192)

    def test_init_(self):
        self.assertTrue(self.song.title, "Punta")
        self.assertTrue(self.song.artist, "Uspurt")
        self.assertTrue(self.song.album, "Pop Folk")
        self.assertTrue(self.song.rating, 1)
        self.assertTrue(self.song.length, 3.45)
        self.assertTrue(self.song.bitrate, 192)

    def test_rate_function(self):
        self.song.rate(4)
        self.assertTrue(self.song.rating, 4)

    def test_rate_function_over(self):
        self.song.rate(6)
        self.assertTrue(self.song.rating, "The rating must be between 1 and 5")

if __name__ == '__main__':
    unittest.main()
