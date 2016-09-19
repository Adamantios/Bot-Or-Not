# noinspection PyPep8Naming
def format_dataset(dataset):
    """Formats the dataset in two lists, containing
    a list of the tweets concatenated in one string for every user
    and a tag indicating if the user is a bot or not, correspondingly.

    dataset -- dictionary - the users dataset."""
    X = []
    y = []

    for user in dataset:
        X.append(''.join(dataset[user][0]))
        y.append(dataset[user][1])

    return X, y
