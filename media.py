import webbrowser

class Movie():
    """ Blueprint of how each movie object will have and do """
    def __init__(self, movie_title, movie_storyline, movie_poster_image_url, movie_youtube_trailer_url):
          self.title = movie_title
          self.storyline = movie_storyline
          self.poster_image_url = movie_poster_image_url
          self.trailer_youtube_url = movie_youtube_trailer_url

    def show_trailer(self):
        """ Method for opening the correspondig html file in web browser """
        webbrowser.open(self.trailer_youtube_url)