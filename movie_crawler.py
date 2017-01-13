# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup
from connection import engine
from commentDAO import commentDAO
from movie_info_crawl import movie_info_crawl
from movie_infoDAO import movie_infoDAO
from movie_comment_crawl import movie_comment_crawl


# crawl links for comment and movie's information
class movie_crawler(object):
    def __init__(self, movie_comment_crawl, movie_info_crawl):
        self.movie_comment_crawl = movie_comment_crawl
        self.movie_info_crawl = movie_info_crawl

    # extract links to get movie's information
    def make_link(self, source):
        temp = source.find('tr')
        first = 'http://movie.naver.com/movie/point/af/list.nhn'
        second = str(temp.find('a')['href'])
        link = first + second
        return link

    # crawling on pages
    def crawl_page(self):
        count = 1
        while(True):
            res = requests\
                    .get(
                         'http://movie.naver.com/movie/point/af/list.nhn?&page={}'
                         .format(count)
                         )
            content = res.text
            soup = BeautifulSoup(content, 'html.parser')
            comment_list = soup.find('tbody')
            count += 1
            if comment_list is None:
                print 'Page End'
                break
            print count
            self.movie_comment_crawl.show_comment(comment_list)
            movie_link = self.make_link(comment_list)
            self.movie_info_crawl.info_crawl(movie_link)


# Operation
if __name__ == '__main__':
    commentDAO = commentDAO()
    movie_infoDAO = movie_infoDAO()
    movie_comment_crawl = movie_comment_crawl(commentDAO)
    movie_info_crawl = movie_info_crawl(movie_infoDAO)
    test = movie_crawler(movie_comment_crawl, movie_info_crawl)
    test.crawl_page()
