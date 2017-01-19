# -*- coding: utf-8 -*-

import re
import requests

from bs4 import BeautifulSoup
from model import movie_info
from connection import Session
from commentDAO import commentDAO


# crawling comments about movie
class movie_comment_crawl(object):
    def __init__(self, commentDAO):
        # Duplication of comment saving is prevented
        self.commentDAO = commentDAO

    def extract_code(self):
        session = Session()
        code_list = session.query(movie_info.code).all()
        for code in code_list:
            self.show_comment(code[0])

    # get number, movie's title, point and comment
    def show_comment(self, code):
        for page in range(1, 21):
            link = 'http://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword={}&target=after&page={}'\
                   .format(code, page)
            res = requests.get(link)
            content = res.text
            soup = BeautifulSoup(content, 'html.parser').find('tbody')

            for item in soup.find_all('tr'):
                primary = item.find('td', attrs={'class': 'ac num'}).get_text()
                title = item.find('a', attrs={'class': 'movie'}).get_text()
                point = item.find('td', attrs={'class': 'point'}).get_text()
                comment = re.sub(
                                 r'\n\s*\n', r'\n\n',
                                 item.find('br').get_text().strip(), flags=re.M
                                )[:-10]
                if self.commentDAO.save_comment(
                                                id=primary,
                                                title=title,
                                                point=point,
                                                comment=comment
                                                ):
                    continue
                else:
                    print 'No updata'
                    break

if __name__ == '__main__':
    commentDAO = commentDAO()
    test = movie_comment_crawl(commentDAO)
    test.extract_code()
