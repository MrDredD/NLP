PATH_TO_CORPUS = "data/prepared.txt"


def get_corpus():
    f = open(PATH_TO_CORPUS, 'r')
    return f.readlines()