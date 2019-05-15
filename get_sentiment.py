from load_model import load_model
def get_sentiment(data):
    clf = load_model()
    if clf.predict([data]) == 1:
        return 'positive'
    else:
        return 'negative'