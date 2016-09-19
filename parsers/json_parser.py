import json
import os


def parse_tweets(folder):
    """Parses all the users json files from a folder.

    folder -- string - the path to the folder containing the json files.

    Returns a dictionary containing a list with the tweets and a bot or not tag for every user.
    """
    dataset = {}

    for filename in os.listdir(folder):

        with open(folder + '/' + filename) as data_file:
            data = json.load(data_file)
            username = filename.replace('.json', '')
            dataset[username] = [data[username]['user_tweets'], data[username]['is_bot']]

    return dataset
