from sklearn.externals import joblib
PATH_TO_MODEL = "models/clf.pkl"


def load_model():
    return joblib.load(PATH_TO_MODEL)
