from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.svm import LinearSVC

from models.soac_model import SOACModel


# noinspection SpellCheckingInspection
def soac_linear_svc():
    """Return a model combining SOAC Model with Linear SVC"""
    feature_union = FeatureUnion([('soac_model', SOACModel())])
    features = ('features', feature_union)
    classifier = ('svm', LinearSVC(C=0.1, class_weight='balanced'))
    estimator = [features, classifier]
    model = Pipeline(estimator)
    return model, str(estimator)
