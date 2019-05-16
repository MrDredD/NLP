from preprocess import preprocessing
from compute_result import compute_tfidf
from get_corpus import get_corpus
from get_sentiment import get_sentiment

KEYWORD_AMOUNT = 6                  # May be empty, better not to


def main():    
    document_to_process = []   
    for doc_name in document_to_process:
        doc = preprocessing(doc_name)
        keywords = compute_tfidf(get_corpus(), doc, KEYWORD_AMOUNT)
        sentiment = get_sentiment(doc)
        print("\nAbstract:")
        print(doc)
        print("\nSentiment:")
        print(sentiment)
        print("\nKeywords:")
        for k in keywords:
            print(k, keywords[k])
        print("==================")
    return


if __name__ == '__main__':
    main()
