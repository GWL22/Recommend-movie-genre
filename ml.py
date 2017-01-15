# coding=utf-8

from model import movie_info, comments
from connection import Session

import sys
import nltk
import many_stop_words as many_stop_words

from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import cross_val_score, train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from konlpy.tag import Twitter
from konlpy.utils import pprint

from gensim.models import doc2vec
from gensim.models.doc2vec import TaggedDocument

from matplotlib import font_manager, rc

reload(sys)
sys.setdefaultencoding('utf-8')

session = Session()
twitter = Twitter()


class machine_learning(object):
    def __init__(self):
        pass

    def make_train_origin(self):
        train_origin = session.query(comments.comment, movie_info.genre) \
                              .join(movie_info, movie_info.title == comments.title) \
                              .filter(comments.point > 7) \
                              .all()
        return train_origin

    def tokenize(self, doc):
        return ['/'.join(tag) for tag in twitter.pos(doc)]

    def train_tokens(self, train_origin):
        return [(self.tokenize(row[0]), row[1]) for row in train_origin]

    def selected_words(self, train_tokens):
        tokens = [tag for data in train_tokens for tag in data[0]]
        text = nltk.Text(tokens, name='NSMC')
        words_list = [f[0] for f in text.vocab().most_common(50)]
        return words_list

    def make_token_list(self, train_tokens):
        return [tag for data in train_tokens for tag in data[0]]
