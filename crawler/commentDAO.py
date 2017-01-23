# -*- coding: utf-8 -*-

from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker
from model import comments
from connection import Session

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# check and save if comment crawled is passed
class commentDAO(object):
    def __init__(self):
        pass

    def save_comment(self, id, title, point, comment):
        session = Session()
        if not self.get_comment_by_id(id):
            print id
            print title
            print 'point: ' + point
            print comment
            print '='*70
            data = comments(
                            ID=id,
                            title=title.encode('utf-8'),
                            point=point,
                            comment=comment.encode('utf-8')
                            )
            session.add(data)
            session.commit()
            return True
        else:
            return False
        session.close()

    # check comment whether on DB or not
    def get_comment_by_id(self, comment_id):
        try:
            session = Session()
            row = session.query(comments) \
                         .filter(comments.ID == comment_id) \
                         .first()
            return row
        except Exception as e:
            print e
        finally:
            session.close()
