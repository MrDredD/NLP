import os
from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename

from preprocess import preprocessing
from compute_result import compute_tfidf
from get_corpus import get_corpus
from get_sentiment import get_sentiment

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
KEYWORD_AMOUNT = 6

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("upload.html")


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    target = os.path.join(APP_ROOT, 'texts/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        #file.save(destination)
    return render_template("complete.html")


#separate func ()
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



@app.route("/about")
def about():
    return render_template("about_us.html")




#KEYWORD_AMOUNT = 6                  # May be empty, better not to


if __name__ == "__main__":
    app.run(port=4555, debug=True)
