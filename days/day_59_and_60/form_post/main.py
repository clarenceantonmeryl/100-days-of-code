from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data)
        print(data['email'])
        print(data['password'])
        return render_template('contact.html', method="POST")
    else:
        return render_template('contact.html', method="GET")


if __name__ == "__main__":
    app.run(debug=True)
    print("done")