# -*- coding: utf-8 -8-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

server = 'ec2-52-41-252-180.us-west-2.compute.amazonaws.com'

connection_string = 'mysql+mysqldb://root:windows48@{}:3306/naver_movie'\
                    .format(server)

engine = create_engine(connection_string, pool_recycle=3600, encoding='utf-8')
Session = sessionmaker(bind=engine)
