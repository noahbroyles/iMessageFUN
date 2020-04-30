from nltk import tokenize
import re


def getVerses(path):
    with open(path, 'r') as f:
        kjv = f.read()
    pattern = re.compile(r"(\d+:\d+.*?)\n\n", re.MULTILINE | re.DOTALL)
    return [x.replace("\n", ' ') for x in pattern.findall(kjv)]


def getWords(path):
    with open(path, 'r') as f:
        text = f.read()
    return [word.replace("\n", ' ') for word in text.split(' ')]


def getSentences(path):
    with open(path, 'r') as f:
        text = f.read()
    return [s.replace("\n", ' ') for s in tokenize.sent_tokenize(text)]


def getLines(path):
    with open(path, 'r') as f:
        text = f.read()
    return [x.replace("\n", '') for x in text.split("\n")]
