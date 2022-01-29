from flask import Flask, render_template, request
import requests
import smtplib

my_email = "c.antonmeryl.123@gmail.com"
password = "Almond123"


def send_message(email, message, phone, name):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            to_addrs=my_email,
            from_addr=my_email,
            msg=f"Subject:{email}\n{message}\nfrom,\n{name}\n{phone}"
        )

app = Flask(__name__)


NPOINT_URL = "https://api.npoint.io/5be6380bfdf24dff6d34"
# https://www.npoint.io/docs/5be6380bfdf24dff6d34

response = requests.get(url=NPOINT_URL)
response.raise_for_status()
blogs = response.json()

@app.route('/')
def home():
    return render_template('index.html', blogs=blogs)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        send_message(name=name, email=email, phone=phone, message=message)

    return render_template('contact.html', method=request.method)

@app.route('/post/<int:id>')
def post(id):
    post = None
    for blog in blogs:
        if blog['id'] == id:
            post = blog
            break
    return render_template('post.html', blog=post)


if __name__ == "__main__":
    app.run(debug=True)
    print("done")

