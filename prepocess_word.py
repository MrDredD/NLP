from pymystem3 import Mystem
from nltk.corpus import stopwords
from string import punctuation
import re


def preprocess(word):
    stem = Mystem()
    stop = set(stopwords.words("russian"))
    stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '#', '№', '*', '_', '\n'])
    param = re.sub('[^a-zA-Zа-яА-Я]', ' ', word)
    param.lower()
    param = stem.lemmatize(param)
    param = [token for token in param if token not in stop and token != " " and token.strip() not in punctuation]
    word = " ".join(param)
    word = ' '.join(word for word in word.split() if len(word) > 3)
    return word
