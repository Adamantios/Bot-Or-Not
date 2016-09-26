from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.svm import LinearSVC
from models.soac_model import SOACModel
from preprocess.preprocessor import FunctionWrapper, preprocess_tweets


def soac_linear_svc():
    """Return a model combining SOAC Model with Linear SVC"""
    preprocessing = FunctionWrapper(preprocess_tweets)
    preprocessor = ('preprocessing', preprocessing)
    feature_union = FeatureUnion([('soac_model', SOACModel())])
    features = ('features', feature_union)
    classifier = ('svm', LinearSVC())
    params = {'svm__C': [0.1], 'svm__class_weight': ['balanced']}
    estimator = [preprocessor, features, classifier]
    model = Pipeline(estimator)
    return model, params


def tfidf_vectorizer_linear_svc():
    """Return a simple model combining TfidfVectorizer with Linear SVC"""
    preprocessing = FunctionWrapper(preprocess_tweets)
    preprocessor = ('preprocessing', preprocessing)
    feature_union = FeatureUnion([('tf-idf', TfidfVectorizer())])
    features = ('features', feature_union)
    classifier = ('svm', LinearSVC())
    params = {'svm__C': [0.1], 'svm__class_weight': ['balanced'],
              'features__tf-idf__ngram_range': [(1, 1), (2, 2), (3, 3)]}
    estimator = [preprocessor, features, classifier]
    model = Pipeline(estimator)
    return model, params
