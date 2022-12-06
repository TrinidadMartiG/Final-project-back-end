from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Media, Text_FirstSection, Text_SecondSection, Text_ThirdSection, Text_FourthSection

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///final-project.db"
db.init_app(app)
CORS(app)
Migrate(app, db)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/users", methods=['GET'])
def get_all_users():
    all_user = User.query.all()
    serialize_list = list(map(lambda user: user.serialize(), all_user))
    response_body = {
        "msg":  "Get /user response was successful"
    }

    return jsonify(serialize_list), 201


@app.route("/create_user", methods=["POST"])
def create_user():
    user = User()
    user.name = request.json.get("name")
    user.email = request.json.get("email")
    user.password = request.json.get("password")
   # user.is_active = request.json.get("is_active")
    db.session.add(user)
    db.session.commit()
    return 'User registered', 202

#routes for first section
@app.route("/send_data_firstsection", methods=["POST"])
def send_data_firstsection():
    data = Text_FirstSection()
    data.id = request.json.get("id")
    data.user_id = request.json.get("user_id")
    data.mainTitle = request.json.get("mainTitle")
    data.mainDescription = request.json.get("mainDescription")
    db.session.add(data)
    db.session.commit()
    return 'data sended', 202


@app.route("/update_data_firstsection/<int:user>", methods=["PUT"])
def update_data_firstsection(user=None):
    if user is not None:
        print(user)
        text_firstsection = Text_FirstSection.query.filter_by(user_id=user).all()
        print(text_firstsection)
        text_firstsection.mainTitle = request.json.get("mainTitle")
        text_firstsection.mainDescription = request.json.get("mainDescription")
        db.session.commit()
        return 'data updated', 202


@app.route("/get_data_firstsection/<int:user>", methods=["GET"])
def get_data_firstsection(user=None):
    if user is not None:
        text_firstsection = Text_FirstSection.query.filter_by(user_id=user).first()
        #serialize_list = list(
            #map(lambda text_firstsection: text_firstsection.serialize(), all_data))
       # response_body = {
        #    "msg":  "Get /data response was successful"
        #}
        print(text_firstsection)
        serializer = text_firstsection.serialize()
        print(serializer)
        return (serializer), 201


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
