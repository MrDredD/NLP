from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template("upload.html")

@app.route('/loading')
def upload_file():
    return render_template("complete.html", keyword=keywords, emo=color)


@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
