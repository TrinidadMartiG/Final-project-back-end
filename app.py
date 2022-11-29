from flask import Flask, jsonify, request, render_template
from flask_cors import CORS 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy 
from models import db, User, Media, Text

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
    user.is_active = request.json.get("is_active")
    db.session.add(user)
    db.session.commit()
    return 'User registered',202

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)