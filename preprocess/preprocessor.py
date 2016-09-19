from preprocess.methods import clean_html, detwittify, remove_numbers, remove_punctuation, remove_links


def preprocess_tweets(tweets):
    """Preprocess the tweets and return them "clean".

    tweets -- list - the tweets list to be cleaned."""
    tweets = clean_html(tweets)
    tweets = detwittify(tweets)
    tweets = remove_numbers(tweets)
    tweets = remove_punctuation(tweets)
    tweets = remove_links(tweets)
    return tweets
