from argparse import ArgumentParser


# noinspection SpellCheckingInspection
def parse_arguments():
    """Returns the program's input arguments."""
    parser = ArgumentParser(description='Trains a model to identify twitter bots')
    parser.add_argument('-i', '--input', type=str,
                        required=True, dest='in_folder',
                        help='path to folder with pan dataset for a language')
    parser.add_argument('-n', '--numfolds', type=int,
                        dest='num_folds', default=4,
                        help='Number of folds to use in cross validation')

    return parser.parse_args()
