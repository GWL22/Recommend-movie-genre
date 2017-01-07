# -*- coding: utf-8 -*-

import sys
import os
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import Column, ForeignKey, Integer, CHAR, String

reload(sys)
sys.setdefaultencoding('utf-8')

Base = declarative_base()


class comments(Base):
    __tablename__ = 'comments'

    ID            = Column(Integer, nullable=False, primary_key=True)
    title         = Column(CHAR(200), nullable=False)
    point         = Column(Integer, nullable=False, default=0)
    comment       = Column(String(200), nullable=True, default=None)


class movie_info(Base):
    __tablename__ = 'movie_info'

    title         = Column(CHAR(200), primary_key=True, nullable=False)
    genre         = Column(CHAR(200), nullable=False)
