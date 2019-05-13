import nltk
# nltk.download("stopwords")

from pymystem3 import Mystem
from nltk.corpus import stopwords
from string import punctuation
from bs4 import BeautifulSoup
import os
import re

stem = Mystem()
stop = set(stopwords.words("russian"))
stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '#', '№', '*', '_', '\n'])

path = "data/ffs"
total_corpus = []
corpus = []
PATHS = []
PREPARED_CORPUS_PATH = 'data/prepared_corpus.txt'


def preprocess_text(input_text):
    param = re.sub('[^a-zA-Zа-яА-Я]', ' ', input_text)
    param.lower()
    param = stem.lemmatize(param)
    param = [token for token in param if token not in stop and token != " " and token.strip() not in punctuation]
    input_text = " ".join(param)
    return input_text


for directories in os.listdir(path):
    PATHS.append(os.path.join(path, directories))

f = open(PREPARED_CORPUS_PATH, 'a')
count = 0
for dirname in PATHS:
    for filename in os.listdir(dirname):
        html_report_part1 = open(os.path.join(dirname, filename), 'r')
        soup = BeautifulSoup(html_report_part1, 'html.parser')
        text = preprocess_text(soup.get_text())
        text = ' '.join(word for word in text.split() if len(word) > 3)
        corpus.append(text)
        total_corpus.append(text.split())
        print("File " + str(os.path.join(dirname, filename)) + " processed")
        f.writelines(text)
        # print(text)
        count += 1
        print(str(100*count/2207) + "%")
    print("Directory " + dirname + " processed")
f.close()

PREPARED_PATH = 'data/prepared.txt'
f = open(PREPARED_PATH, 'w')
for i in range(0, len(corpus)):
    f.write(corpus[i] + "\n")
f.close()

for i in range(0, len(total_corpus)):
    single_document = ""
    for j in range(0, len(total_corpus[i])):
        if single_document == "":
            single_document = total_corpus[i][j]
        else:
            single_document += " " + total_corpus[i][j]
    corpus.append(single_document)

