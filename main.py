from preprocess import preprocessing
from compute_result import compute_tfidf
from get_corpus import get_corpus
from get_sentiment import get_sentiment


def main():
    DOCUMENT_TO_PROCESS = "001.htm"
    doc = preprocessing(DOCUMENT_TO_PROCESS)
    keywords = compute_tfidf(get_corpus(), doc, 5)
    sentiment = get_sentiment(doc)
    print("\nAbstract:")
    print(doc)
    print("\nSentiment:")
    print(sentiment)
    print("\nKeywords:")
    for k in keywords:
        print(k, keywords[k])
    return
if __name__ == '__main__':
    main()
