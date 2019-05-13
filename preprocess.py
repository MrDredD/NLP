import nltk
# nltk.download("stopwords")

from pymystem3 import Mystem
from nltk.corpus import stopwords
from string import punctuation
import re
from bs4 import BeautifulSoup


def preprocessing(path):
    stem = Mystem()
    stop = set(stopwords.words("russian"))
    stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '#', '№', '*', '_', '\n'])

    def preprocess_text(input_text):
        param = re.sub('[^a-zA-Zа-яА-Я]', ' ', input_text)
        param.lower()
        param = stem.lemmatize(param)
        param = [token for token in param if token not in stop and token != " " and token.strip() not in punctuation]
        input_text = " ".join(param)
        input_text = ' '.join(word for word in input_text.split() if len(word) > 3)

        return input_text

    html_report_part1 = open(path, 'r')
    soup = BeautifulSoup(html_report_part1, 'html.parser')
    return preprocess_text(soup.get_text())
