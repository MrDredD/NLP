from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from scipy.sparse import coo_matrix
from nltk.corpus import stopwords
from string import punctuation
from bs4 import BeautifulSoup
from pymystem3 import Mystem
import re


def compute_tfidf(corpus, preprcessed_document, keyword_amount=5):
    stop = set(stopwords.words("russian"))
    stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '#', '№', '*', '_', '\n'])
    cv = CountVectorizer(max_df=0.8, stop_words=stop, max_features=10000, ngram_range=(1,3))
    X = cv.fit_transform(corpus)

    tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
    tfidf_transformer.fit(X)

    feature_names = cv.get_feature_names()
    tf_idf_vector = tfidf_transformer.transform(cv.transform([preprcessed_document]))

    def sort_coo(coo_matrix):
        tuples = zip(coo_matrix.col, coo_matrix.data)
        return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

    def extract_topn_from_vector(feature_names, sorted_items, keyword_amount):
        """get the feature names and tf-idf score of top n items"""

        # use only topn items from vector
        sorted_items = sorted_items[:keyword_amount]

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
    return extract_topn_from_vector(feature_names, sorted_items, keyword_amount)

