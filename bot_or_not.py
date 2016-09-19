import datetime
import time

from models.create_model import soac_linear_svc
from parsers.arguments_parser import parse_arguments
from parsers.json_parser import parse_tweets
from utilities.file_management import log
from validation.grid_search_cv import cross_validation


def main():
    args = parse_arguments()
    task = 'Bot detection'
    time_start = time.time()
    timestamp = str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')).split('.')[0]

    log('------------- Created at: ' + timestamp + ' -------------')
    log('Loading dataset...')
    tweets_dataset = parse_tweets(args.in_folder)

    log('Loaded %s users...' % len(tweets_dataset))
    log('Creating model for %s...' % task)
    model, model_name = soac_linear_svc()

    log('\n---------------- Performing Grid Search CV ----------------')
    results = cross_validation(tweets_dataset, model, args.num_folds)

    log('\n------------------------- Results -------------------------')
    log('Results for %s with estimator:\n %s' % (task, model_name))
    log('Grid Scores: ' + results)

    log('Runtime: {} seconds.\n\n'.format(str(time.time() - time_start)))

    print 'The results have been written in \'results.txt\', in \'results\' folder.'


if __name__ == '__main__':
    main()
