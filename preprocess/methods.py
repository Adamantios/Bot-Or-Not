import regex


def clean_html(tweets):
    """Strips html.

    tweets -- collection - the collection of tweets to clean.

    Returns list of tweets cleaned from html.
    """
    return [regex.sub('(\\<.*?\\>)', '', text) for text in tweets if text is not None]


def detwittify(tweets):
    """Remove characteristics which aren't "natural" text, like hashtags, urls and usernames.

    tweets -- collection - the tweets to clean.

    Returns list of tweets cleaned from specific characteristics.
    """

    # Regexps to capture hashtags, replies and urls
    url_regex = regex.compile(r'(?P<all>\s?(?P<url>(https?|ftp)://[^\s/$.?#].[^\s]*))')
    hashtag_regex = regex.compile(r'(?<=\s+|^)(?P<all>#(?P<content>\w+))', regex.UNICODE)
    reply_regex = regex.compile(r'(?P<all>(^|\s*)@(?P<content>\w+)\s*?)', regex.UNICODE)
    detwittified = []

    for text in tweets:
        cleaned = url_regex.sub('', text)
        cleaned = hashtag_regex.sub('\g<2>', cleaned)
        cleaned = reply_regex.sub('', cleaned)
        detwittified.append(cleaned.strip())

    return detwittified


def remove_numbers(tweets):
    """Removes numbers from tweets.

    tweets -- collection - the tweets to clean.
    """
    return [regex.sub('[0-9]+', ' ', tweet) for tweet in tweets]


def remove_punctuation(tweets):
    """Removes punctuations from tweets.

    tweets -- collection - the tweets to clean.
    """
    return [regex.sub('[^\P{P}]+', ' ', tweet) for tweet in tweets]


def remove_links(tweets):
    """Removes links from tweets.

    tweets -- collection - the tweets to clean.
    """
    return [tweet.replace('urlLink', '') for tweet in tweets]
