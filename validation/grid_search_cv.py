from sklearn.grid_search import GridSearchCV

from utilities.file_management import log
from utilities.formatter import format_dataset


# noinspection PyPep8Naming
def cross_validation(dataset, params, model, num_folds):
    """Train and cross validate a model

    task -- the task we want to classify for, ex: bot detection"""
    log('\n---------------- Performing Grid Search CV ----------------')

    X, y = format_dataset(dataset)

    log('Parameters: ' + str(params))
    log('Training instances: %s' % (len(X)))
    log('Using %s fold validation.' % num_folds)

    grid_cv = GridSearchCV(model, params, n_jobs=-1, refit=False, cv=num_folds, verbose=1)

    log('Fitting...')
    grid_cv.fit(X, y)

    return str(grid_cv.estimator), str(grid_cv.grid_scores_)
