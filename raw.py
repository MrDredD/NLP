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

thislist = [['omg'], ['look', 'at', 'this', 'face'], ['if', 'u', 'fill']]
anotherlist = []

type(thislist[1])
for i in range(0, len(thislist)):
    single_document = ""
    for j in range(0, len(thislist[i])):
        print(thislist[i])
        print(thislist[i][j])
        if single_document == "":
            single_document = thislist[i][j]
        else:
            single_document += " " + thislist[i][j]
    anotherlist.append(single_document)
print(anotherlist)

for i in range(0, len(total_corpus)):
    single_document = ""
    for j in range(0, len(total_corpus[i])):
        if single_document == "":
            single_document = total_corpus[i][j]
        else:
            single_document += " " + total_corpus[i][j]
    corpus.append(single_document)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_df=0.8, stop_words=stop, max_features=10000, ngram_range=(1,3))
X = cv.fit_transform(corpus)

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
tfidf_transformer.fit(X)

feature_names=cv.get_feature_names()

html_report_part2 = open('001.htm', 'r')
soup = BeautifulSoup(html_report_part2, 'html.parser')
doc = preprocess_text(soup.get_text())

tf_idf_vector=tfidf_transformer.transform(cv.transform([doc]))

from scipy.sparse import coo_matrix


def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)


def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """get the feature names and tf-idf score of top n items"""

    # use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []

    # word index and corresponding tf-idf score
    for idx, score in sorted_items:
        # keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    # create a tuples of feature,score
    # results = zip(feature_vals,score_vals)
    results = {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]] = score_vals[idx]

    return results


# sort the tf-idf vectors by descending order of scores
sorted_items = sort_coo(tf_idf_vector.tocoo())
# extract only the top n; n here is 10
keywords = extract_topn_from_vector(feature_names, sorted_items, 10)

# now print the results
print("\nAbstract:")
print(doc)
print("\nKeywords:")
for k in keywords:
    print(k, keywords[k])

PREPARED_PATH = 'data/prepared.txt'
f = open(PREPARED_PATH, 'w')
for i in range(0, len(corpus)):
    f.write(corpus[i] + "\n")
f.close()
corpusyara = []

f = open(PREPARED_PATH)
text123 = f.readlines()
for i in range(0, len(text123)):
    corpusyara.append(text123[i])
print(corpusyara)
f.close()
