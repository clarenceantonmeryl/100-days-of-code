from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



##CREATE TABLE
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


def get_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return random_cafe


@app.route("/random")
def get_random_cafe():
    random_cafe = get_cafe()
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search/<string:q>")
def search(q:str):
    cafe = db.session.query(Cafe).filter_by(location=q).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Error": "Not found"}), 404


@app.route("/add", methods=["POST"])
def add():
    data = request.form

    print(data.get("name"))
    print(data.get("has_toilet"))
    print(bool(data.get("has_toilet")))

    new_cafe = Cafe(
        name=data.get("name"),
        map_url=data.get("map_url"),
        img_url=data.get("img_url"),
        location=data.get("location"),
        seats=data.get("seats"),
        has_toilet=bool(data.get("has_toilet")),
        has_wifi=True,
        has_sockets=True,
        can_take_calls=True,
        coffee_price=data.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe!"})


@app.route("/update-price/<int:id>", methods=["PATCH"])
def patch_price(id):
    cafe = db.session.query(Cafe).get(id)
    if cafe:
        # data = request.form
        data = request.args
        print(data.get("price"))
        cafe.coffee_price = data.get("price")
        db.session.commit()
        return jsonify(response={"success": "Successfully patched the new cafe!"})
    else:
        return jsonify(error={"Error": "Not found"}), 404


@app.route("/delete-cafe/<int:id>", methods=["DELETE"])
def delete_cafe(id):
    cafe = db.session.query(Cafe).get(id)
    if cafe:
        data = request.args
        if data.get("api-key") == "TopSecretAPIKey":
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the new cafe!"})
        else:
            return jsonify(error={"Error": "Unauthorised"}), 403
    else:
        return jsonify(error={"Error": "Not found"}), 404




## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
