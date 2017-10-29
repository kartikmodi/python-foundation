import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from html_code_gen_api import fresh_tomatoes
'''
Created on Sep 17, 2017

@author: workstation
'''


class Movie(object):
    '''
    Class to represent a movie.
    '''

    def __init__(self, title, poster_image_url, trailer_youtube_url, storyline=''):
        '''
        Calls when object is created. Sets attributes of the objects
        '''
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.storyline = storyline


bhoomi = Movie('Bhoomi', 'https://3.bp.blogspot.com/-UNsQoyz-InI/WXxJi3EuoOI/AAAAAAAAOls/tTefcm4VDFAWNFZl1Tc3eV3LODzbJC5VgCLcBGAs/s1600/bhoomi-sanjay-dutt-upcoming-movie-poster-release-date-star-cast-poster-mt-wiki-2017.jpg',
               'https://www.youtube.com/watch?v=AgiFCRU0MXg', 'Dummy Story Line 1')
the_man_who_knew_infinity = Movie('The Man who knew Infinity', 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d8/The_Man_Who_Knew_Infinity_%28film%29.jpg/220px-The_Man_Who_Knew_Infinity_%28film%29.jpg',
                                  'https://www.youtube.com/watch?v=oXGm9Vlfx4w', 'Dummy Story Line 2')
movies = [bhoomi, the_man_who_knew_infinity]
# This function call opens a page of movies generated
# from the input, a list of movie instances.
fresh_tomatoes.open_movies_page(movies)
