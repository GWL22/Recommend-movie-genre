# -*- coding: utf-8 -*-

from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker
from model import movie_info
from connection import Session

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# the data crawled checking and save
class movie_infoDAO(object):
    def __init__(self):
        pass

    # save movie info if DataBase has not
    def save_movie_info(self, title, genre):
        session = Session()
        if not self.get_movie_by_title(title):
            print title
            print 'genre: ' + genre
            print '='*70
            data = movie_info(
                              title=title,
                              genre=genre
                             )
            session.add(data)
            session.commit()
            return True
        else:
            return False
        session.close()

    # check whether Database has movie info already or not
    def get_movie_by_title(self, movie_title):
        try:
            session = Session()
            row = session.query(movie_info) \
                         .filter(movie_info.title == movie_title) \
                         .first()
            return row
        except Exception as e:
            print e
        finally:
            session.close()
