from sklearn.base import BaseEstimator, TransformerMixin

from preprocess.methods import clean_html, detweettify, remove_numbers, remove_punctuation, remove_links
from utilities.file_management import log


def preprocess_tweets(tweets):
    """Preprocess the tweets and return them "clean".

    tweets -- list - the tweets list to be cleaned."""
    tweets = clean_html(tweets)
    tweets = detweettify(tweets)
    tweets = remove_numbers(tweets)
    tweets = remove_punctuation(tweets)
    tweets = remove_links(tweets)
    return tweets


# noinspection PyPep8Naming
class FunctionWrapper(BaseEstimator, TransformerMixin):
    """ Class to wrap around a function in order to be used in sklearn's pipeline

    Attributes:
        function : The function to be wrapped around
    """

    def __init__(self, function):
        self.function = function

    # noinspection PyUnusedLocal
    def fit(self, X, y):
        """ No need to fit"""

        return self

    def transform(self, X):
        """ Transform data

        X - The input to transform
        returns - A transformation of X implemented in function
        """
        X = self.function(X)
        return X
