from nltk import tokenize
import re


def getVerses(path):
    with open(path, 'r') as f:
        kjv = f.read()
    pattern = re.compile(r"(\d+:\d+.*?)\n\n", re.MULTILINE | re.DOTALL)
    verses = [x.replace("\n", ' ') for x in pattern.findall(kjv)]
    return verses


def getWords(path):
    with open(path, 'r') as f:
        text = f.read()
    words = [word.replace("\n", ' ') for word in text.split(' ')]
    return words


def getSentences(path):
    with open(path, 'r') as f:
        text = f.read()
    sentences = [s.replace("\n", ' ') for s in tokenize.sent_tokenize(text)]
    return sentences


def getLines(path):
    with open(path, 'r') as f:
        text = f.read()
    lines = [x.replace("\n", '') for x in text.split("\n")]
    return lines
