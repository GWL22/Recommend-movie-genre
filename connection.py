# -*- coding: utf-8 -8-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

server = 'add your server address'

my_id = 'your mysql id'
my_pw = 'your mysql password'
my_port = 'your mysql port'
my_schema = 'your schema name will use'
connection_string = 'mysql+mysqldb://{}:{}{}:{}/{}'.format(my_id,
                                                           my_pw,
                                                           my_port,
                                                           my_schema,
                                                           sever)

engine = create_engine(connection_string, pool_recycle=3600, encoding='utf-8')
Session = sessionmaker(bind=engine)
