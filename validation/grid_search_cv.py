from sklearn.grid_search import GridSearchCV

from preprocess.preprocessor import preprocess_tweets
from utilities.file_management import log
from utilities.formatter import format_dataset


# noinspection PyPep8Naming
def cross_validation(dataset, model, num_folds):
    """Train and cross validate a model

    task -- the task we want to classify for, ex: bot detection"""
    X, y = format_dataset(dataset)

    # Get parameters for Grid Search if they exist - else pass empty dict
    params = {}
    log('Parameters: ' + str(params))
    log('Training instances: %s' % (len(X)))
    log('Using %s fold validation.' % num_folds)

    grid_cv = GridSearchCV(model, params, cv=num_folds, verbose=1,
                           n_jobs=-1, refit=False)

    log('Preprocessing...')
    X = preprocess_tweets(X)

    log('Fitting...')
    grid_cv.fit(X, y)

    return str(grid_cv.grid_scores_)
