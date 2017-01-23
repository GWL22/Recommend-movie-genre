# coding=utf-8

import re
import requests

from bs4 import BeautifulSoup
from connection import engine
from movie_infoDAO import movie_infoDAO


def find_a(tags):
    return tags.name == 'a' and tags.has_attr('href')


class movie_code_crawler(object):
    def __init__(self, movie_infoDAO):
        self.movie_infoDAO = movie_infoDAO

    def extract_code(self, tag):
        num = 1
        while True:

            link = 'http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date={}&tg={}&page={}'\
                   .format('20170117', str(tag), str(num))

            res = requests.get(link)
            content = res.text
            soup = BeautifulSoup(content, 'html.parser')
            content_list = soup.find_all('td', attrs={'class': 'title'})

            if num > 16:
                print 'Page End'
                break

            for row in content_list:
                item = row.find(find_a)
                if item is not None:
                    match = re.search(r'code=\d*', item['href'])
                    code = match.group()[5:]  # primary key of movie
                    title = item.get_text().encode('utf-8')
                    self.movie_infoDAO.save_movie_info(str(title),
                                                       str(tag),
                                                       code)

            num += 1
            print 'page: ' + str(num)

if __name__ == '__main__':
    movie_infoDAO = movie_infoDAO()
    test = movie_code_crawler(movie_infoDAO)
    for num in range(1, 20):
        print 'tag: ' + str(num)
        test.extract_code(num)
    print 'Crawling End'
