class Song:

    MAX_RATING = 5
    MIN_RATING = 1
    LOW_BITRATE = 100

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, rating):
        if rating <= self.MAX_RATING and rating >= self.MIN_RATING:
            self.rating = rating
        else:
            error_message = "The rating must be between {} and {}"
            raise(error_message.format(self.MIN_RATING, self.MAX_RATING))
