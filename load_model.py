PATH_TO_MODEL = "data/clf.pkl"
from sklearn.externals import joblib

def load_model():
    return joblib.load(PATH_TO_MODEL)
