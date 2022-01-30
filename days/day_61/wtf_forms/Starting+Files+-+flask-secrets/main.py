from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField("Login")


app.secret_key = "anything"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    print("LOGIN VALIDATION", login_form.validate_on_submit())

    if login_form.validate_on_submit():
        if login_form.email.data == "a@b.com" and login_form.password.data == "12345678":
            print("VALID DATA")
            return render_template('success.html')
        else:
            print("INVALID DATA")
            return render_template('denied.html')
    else:
        return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)