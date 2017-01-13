# coding=utf-8

import csv
import datetime as dt

from model import comments, movie_info
from connection import Session

# for distinct save file name
save_date = dt.date.today()
# decide save folder path
file_path = './Project/P04_Text_analysis_movie_comment/dataset/'
session = Session()

# Read DB
result = session.query(movie_info.title,
                       movie_info.genre,
                       comments.comment) \
                .join(comments, movie_info.title == comments.title) \
                .filter(comments.point > 7) \
                .all()

try:
    # make file with columns
    with open('{}{}_train.csv'.format(file_path, save_date), 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['title', 'genre', 'comment'])

    # add data
    for row in result:
        with open('{}{}_train.csv'.format(file_path, save_date), 'ab') as csvfile:
            header = ['title', 'genre', 'comment']
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([row[0], row[1], row[2]])

    print 'Made new train on {}'.format(save_date)

except Exception as e:
    print e
