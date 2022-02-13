from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

db = SQLAlchemy(app)

TMDB_API_KEY = "9e08293d3ddfe3fe666b7b9b627f7330"

TMDB_CONFIG_URL = "https://api.themoviedb.org/3/configuration"
# "https://api.themoviedb.org/3/configuration?api_key=9e08293d3ddfe3fe666b7b9b627f7330"

TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
# "https://api.themoviedb.org/3/search/movie?api_key=9e08293d3ddfe3fe666b7b9b627f7330&language=en-US&query=spiderman"

TMDB_DETAIL_URL = "https://api.themoviedb.org/3/movie/"
# "https://api.themoviedb.org/3/movie/634649?api_key=9e08293d3ddfe3fe666b7b9b627f7330&language=en-US"


TMDB_IMAGE_ROOT = "https://image.tmdb.org/t/p/w500"
# https://image.tmdb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg
# https://image.tmdb.org/t/p/original/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'({self.id} {self.title} - {self.rating})'


# db.create_all()

# After adding the new_movie the code needs to be commented out/deleted.
# So you are not trying to add the same movie twice.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


def get_response(url, params):
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()


class AddMovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    add = SubmitField("Add")

@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()
    # Movie.query.order_by(Movie.rating.desc()).all()
    return render_template("index.html", movies=movies)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    movie = Movie.query.get(id)
    if request.method == "POST":
        data = request.form
        movie.rating = float(data['rating'])
        movie.review = data['review']
        db.session.commit()

    return render_template("edit.html", movie=movie)


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddMovieForm()
    if request.method == "POST":
        print(add_form.title.data)
        # api_key=9e08293d3ddfe3fe666b7b9b627f7330&language=en-US&query=spiderman"

        params = {
            "api_key": "9e08293d3ddfe3fe666b7b9b627f7330",
            "language": "en-US",
            "query": add_form.title.data
        }

        response = get_response(url=TMDB_SEARCH_URL, params=params)
        add_movie_list = response["results"]
        print(add_movie_list)

        return render_template("select.html", movies=add_movie_list)

    return render_template("add.html", form=add_form)


@app.route("/delete/<int:id>")
def delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/insert_movie/<int:id>")
def insert_movie(id):
    params = {
        "api_key": "9e08293d3ddfe3fe666b7b9b627f7330",
        "language": "en-US"
    }
    movie_data = get_response(url=f"{TMDB_DETAIL_URL}/{id}", params=params)

    # title = db.Column(db.String(250), unique=True, nullable=False)
    # year = db.Column(db.Integer, nullable=False)
    # description = db.Column(db.String(500), nullable=False)
    # img_url = db.Column(db.String(250), nullable=False)

    movie = Movie(
        title=movie_data["title"],
        year=movie_data["release_date"],
        description=movie_data["overview"],
        img_url=f"{TMDB_IMAGE_ROOT}{movie_data['poster_path']}"
    )

    db.session.add(movie)
    db.session.commit()

    # print(movie["id"], movie["overview"], movie["poster_path"], movie["release_date"])

    return redirect(url_for("edit", id=movie.id))


if __name__ == '__main__':
    app.run(debug=True)
