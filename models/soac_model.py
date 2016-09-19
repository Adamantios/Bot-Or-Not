from collections import Counter

import numpy
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer

from utilities.file_management import log


class SOACModel(BaseEstimator, TransformerMixin):
    """Complementary of SOA model 22"""
    def __init__(self, max_df=1.0, min_df=1, max_features=None, threshold=0.1):
        self.max_df = max_df
        self.min_df = min_df
        self.max_features = max_features
        self.threshold = threshold
        self.term_table = None
        self.labels = None
        self.prior_row = None
        self.counter = TfidfVectorizer(use_idf=True)

    # noinspection PyPep8Naming
    def fit(self, X, y=None):
        if y is None:
            raise ValueError('We need y labels to supervise-fit!')

        else:
            parameters = {
                'input': 'content',
                'encoding': 'utf-8',
                'decode_error': 'ignore',
                'analyzer': 'word',
                'max_df': self.max_df,
                'min_df': self.min_df,
                'max_features': self.max_features
            }
            self.counter.set_params(**parameters)
            doc_term = self.counter.fit_transform(X)
            target_profiles = sorted(list(set(y)))
            self.labels = target_profiles
            dd = Counter(y)
            self.prior_row = numpy.zeros([1, len(target_profiles)])

            for i, key in enumerate(sorted(dd.keys())):
                dd[key] /= float(len(y))
                self.prior_row[0, i] = 1 / dd[key]

            doc_prof = numpy.tile(self.prior_row, (doc_term.shape[0], 1))

            for i in range(0, doc_term.shape[0]):
                doc_prof[i, target_profiles.index(y[i])] = 0

            try:
                doc_term.data = numpy.log2(doc_term.data + 1)

            except Exception, e:
                log('Error in log2')
                log(e)

            try:
                term_prof = doc_term.transpose().dot(doc_prof)
                term_prof = term_prof / term_prof.sum(axis=0)
                term_prof = term_prof / numpy.reshape(term_prof.sum(axis=1), (term_prof.sum(axis=1).shape[0], 1))
                self.term_table = term_prof

            except Exception, e:
                log('Error in product')
                log(e)

            return self

    # noinspection PyPep8Naming
    def transform(self, X):
        if self.labels is None:
            raise AttributeError('term_table was no found! \
             Probably model was not fitted first. Run model.fit(X,y)!')

        else:
            doc_term = self.counter.transform(X)
            doc_prof = doc_term.dot(self.term_table)

            for i in range(0, doc_prof.shape[0]):
                doc_prof[i, :] = doc_prof[i, :]

            return doc_prof
