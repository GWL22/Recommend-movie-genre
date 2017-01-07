# -*- coding: utf-8 -*-

import requests
import re

from bs4 import BeautifulSoup
from connection import engine


class movie_info_crawl(object):
    def __init__(self, movie_infoDAO):
        self.movie_infoDAO = movie_infoDAO

    # crawl movie info and get movie's title and genre
    def info_crawl(self, movie_link):
        res = requests.get(movie_link)
        content = res.text
        soup = BeautifulSoup(content, 'html.parser')
        info_temp = soup.find('div', attrs={'choice_movie_info'})
        movie_title = self.movie_title_crawl(info_temp)
        movie_genre = self.movie_genre_crawl(info_temp)
        self.movie_infoDAO.save_movie_info(movie_title, movie_genre)

    # find movie title
    def movie_title_crawl(self, info_temp):
        movie_title = info_temp.find('h5').get_text().strip()
        return movie_title.encode('utf-8')

    # find movie genre
    def movie_genre_crawl(self, info_temp):
        movie_genre_list = []
        for item in info_temp.find('tr').find('td').find_all('a'):
            genre_temp = item.get_text().strip()
            # filtering others except genre data
            match = re.search(r'\d\d', genre_temp)
            if not match:
                movie_genre_list.append(genre_temp)

        # make a sentence if there are several genre belonged to movie
        movie_genre = self.make_str(movie_genre_list)
        return movie_genre

    # make items to string in the list
    def make_str(self, data_list):
        result = ''
        for num in range(len(data_list)):
            if num == 0:
                result += data_list[num]
            else:
                result += ','+data_list[num]
        return result.encode('utf-8')
