from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

year = datetime.now().year

AGIFY_URL = "https://api.agify.io"
GENDERISE_URL = "https://api.genderize.io"
BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"

#
# def predict_info(name):
#     params = {
#         "name": name
#     }
#     response_age = requests.get(url=AGIFY_URL, params=params)
#     response_age.raise_for_status()
#
#     response_gender = requests.get(url=GENDERISE_URL, params=params)
#     response_gender.raise_for_status()
#
#     return response_age.json().get("age", 0), response_gender.json().get("gender", "unknown")


@app.route('/')
def home():
    number = random.randint(1, 1192093029)
    return render_template('home.html', number=number, year=year)

#
# @app.route("/guess/<string:name>")
# def guess(name: str):
#     age, gender = predict_info(name)
#     return render_template('guess.html', name=name.title(), age=age, gender=gender)


response = requests.get(url=BLOG_URL)
response.raise_for_status()
# blogs_titles = [blog_item['title'] for blog_item in response.json()]
# blogs_subtitles = [blog_item['subtitle'] for blog_item in response.json()]
# blogs_bodies = [blog_item['body'] for blog_item in response.json()]
blogs = response.json()


@app.route('/blog')
def blog():
    return render_template("blog.html", blogs=blogs)


@app.route('/post/<int:id>')
def blog_post(id):

    blog_post: dict = {}

    for blog in blogs:
        if blog['id'] == id:
            blog_post = blog
            break

    print(blog_post)
    return render_template("blog_post.html", blog=blog_post)


if __name__ == "__main__":
    app.run(debug=True)


# {{ url_for('blog') }}/{{ blog['id'] }}
