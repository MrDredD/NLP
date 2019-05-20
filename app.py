import os
from flask import Flask, request, redirect, url_for, render_template


from preprocess import preprocessing
from compute_result import compute_tfidf
from get_corpus import get_corpus
from get_sentiment import get_sentiment

KEYWORD_AMOUNT = 6                  # May be empty, better not to

app = Flask(__name__)

TEXT_UPLOADS = os.path.dirname(os.path.abspath(__file__))
app.config["ALLOWED_EXT"] = ["TXT", "DOCX"]

def allowed_file(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_EXT"]:
        return True
    else:
        return False




@app.route('/upload-text', methods=['POST', 'GET'])
def upload_text():
    target = os.path.join(TEXT_UPLOADS, 'text/')
    print("UUUUUUUU", target)

    if not os.path.isdir(target):
        os.mkdir(target)

    if request.method == "POST":

        if request.files:

            text_file = request.files["fiilee"]
            #print(text_file)

            if text_file.filename == "":
                print("No filename")
                return redirect(request.url)

            if not allowed_file(text_file.filename):
                print("NO SON")
                return redirect(request.url)
            else:
                filename = text_file.filename
                print(filename)

            destination = "/".join([target, filename])
           # print("ffff", destination)
            text_file.save(destination)
            print("File saved")


            #file saves, include main

            document_to_process = []
            document_to_process.append(destination)
            for doc_name in document_to_process:
                print(doc_name)
                print(type(doc_name))#str
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


            return ("complete.html")

    return render_template("upload.html")
if __name__ == '__main__':
    app.run(debug=True)
