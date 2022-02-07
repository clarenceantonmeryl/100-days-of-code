import sqlite3

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

# new_book = Book(title="r", author="a", rating=9.9)
# db.session.add(new_book)
# db.session.commit()

# book = Book.query.filter_by(title="T").first()
# book.title = "T"
# db.session.commit()

# book = Book.query.get(2)  # .filter_by(title="T").first()
# book.title = "R"
# db.session.commit()

book = Book.query.get(2)  # .filter_by(title="T").first()
db.session.delete(book)
db.session.commit()


books = db.session.query(Book).all()
print(books)

# data_base = sqlite3.connect("playground/books-collection.db")
#
# cursor = data_base.cursor()

#         id      INTEGER         PRIMARY_KEY    UNIQUE,

# cursor.execute(
#     """
#     CREATE TABLE books (
#         title   varchar(250)    NOT NULL       UNIQUE,
#         author  varchar(250)    NOT NULL,
#         rating  FLOAT           NOT NULL
#     )
#     """
# )

# cursor.execute(
#     """
#     INSERT INTO books VALUES(
#         "Harry Potter", "JK Rowling", "9.3"
#     )
#     """
# )
# data_base.commit()