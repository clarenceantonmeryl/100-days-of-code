from flask import Flask

import random

app = Flask(__name__)

#
# def make_bold(function):
#     def wrapper(*args, **kwargs):
#         return f"<strong>{function(number=kwargs['number'])}</strong>"
#     return wrapper
#
#
# def make_emphasis(function):
#     def wrapper(*args, **kwargs):
#         return f"<em>{function(number=kwargs['number'])}</em>"
#     return wrapper
#
#
# def make_underline(function):
#     def wrapper(*args, **kwargs):
#         try:
#             return f"<u>{function(number=kwargs['number'])}</u>"
#         except IndexError:
#             return f"<u>{function()}</u>"
#     return wrapper
#
#
# def bokd_content(content):
#     return content


random_number = random.randint(0, 9)


@app.route('/')
def home():
    return "Guess a number between 0 and 9"


@app.route('/<int:number>')
def display_number(number):
    if number > random_number:
        return "<h1>Too high</h1>"
    elif number < random_number:
        return "<h1>Too low</h1>"
    else:
        return "<h1>Correct answer</h1>"


if __name__ == "__main__":
    app.run(debug=True)
