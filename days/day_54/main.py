# Change directory to the current directory
# export FLASK_APP=main.py
# flask run
#
#
# from flask import Flask
#
# app = Flask(__name__)
#
# print(__name__)
#
# @app.route('/')
# def hello_world():
#     return "hello world"
#
#
# @app.route('/contactus')
# def contact_us():
#     return "Contact Us Here"
#
#
# if __name__ == "__main__":
#     app.run()


def decorator_function(function):
    def wrapper_function():
        print("Starting to greet")
        print(function())
        print("Alright now all done. See you later")

    return wrapper_function


@decorator_function
def greeting():
    return "Greeting Function"


greeting()
