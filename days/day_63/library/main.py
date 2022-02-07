from flask import Flask, render_template, request, redirect, url_for

from flask import Flask

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'({self.id} {self.title} - {self.author} - {self.rating})'


# db.create_all()

all_books = []


@app.route('/')
def home():
    books = db.session.query(Book).all()
    return render_template("index.html", library=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.form
        book = Book(
            title=data["book_name"],
            author=data["author"],
            rating=float(data["rating"])
        )

        db.session.add(book)
        db.session.commit()

    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    print("ID", id)

    book = Book.query.get(id)
    print("Book", book)

    if request.method == "POST":
        data = request.form
        book.rating = float(data["rating"])
        db.session.commit()
    return render_template("edit.html", book=book)


if __name__ == "__main__":
    app.run(debug=True)

