import webbrowser


class Movie():
    """ This class provides a way to store movie related information """

    """Constructor"""
    def __init__(self, title, storyline,
                 poster_image_url, trailer_youtube_url,
                 position, year, imdb_rating, imdb_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.position = position
        self.year = year
        self.imdb_rating = imdb_rating
        self.imdb_url = imdb_url

    """Open a web browser and set the url to the
       trailer of the current movie"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
