# -*- coding: utf-8 -*-

import re

from bs4 import BeautifulSoup


# crawling comments about movie
class movie_comment_crawl(object):
    def __init__(self, commentDAO):
        # Duplication of comment saving is prevented
        self.commentDAO = commentDAO

    # get number, movie's title, point and comment
    def show_comment(self, comment_list):
        for item in comment_list.find_all('tr'):
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
