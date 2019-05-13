from preprocess import preprocessing
from compute_result import compute_tfidf
from get_corpus import get_corpus


def main():
    DOCUMENT_TO_PROCESS = "001.htm"
    doc = preprocessing(DOCUMENT_TO_PROCESS)
    keywords = compute_tfidf(get_corpus(), doc, 5)
    print("\nAbstract:")
    print(doc)
    print("\nKeywords:")
    for k in keywords:
        print(k, keywords[k])
    return


if __name__ == '__main__':
    main()
