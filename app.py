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

@app.route("/login", methods=['POST'])
def login():
    return jsonify(serialize_list), 201

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


@app.route("/get_data_firstsection", methods=["GET"])
def get_data_firstsection():
        text_firstsection = Text_FirstSection.query.all()
        serialize_list = list(map(lambda text_firstsection: text_firstsection.serialize(), text_firstsection))
        response_body = {
            "msg":  "Get /data response was successful"
        }
        return jsonify(serialize_list), 201

@app.route("/data_firstsection/<int:user>", methods=["GET"])
def data_firstsection_byID(user=None):
        text_firstsection = Text_FirstSection.query.filter_by(user_id=user).all()
        serialize_list = list(map(lambda text_firstsection: text_firstsection.serialize(), text_firstsection))
        return jsonify(serialize_list), 201

##routes secondSection##
@app.route("/send_data_secondsection", methods=["POST"])
def send_data_secondsection():
    data = Text_SecondSection()
    data.id = request.json.get("id")
    data.user_id = request.json.get("user_id")
    data.secondSection_MainTitle = request.json.get("secondSection_MainTitle")
    data.secondSection_Description = request.json.get("secondSection_Description")
    data.secondSection_ConceptOne = request.json.get("secondSection_ConceptOne")
    data.secondSection_ConceptTwo = request.json.get("secondSection_ConceptTwo")
    data.secondSection_ConceptThree = request.json.get("secondSection_ConceptThree")
    data.secondSection_ConceptFour = request.json.get("secondSection_ConceptFour")
    data.secondSection_ConceptFive = request.json.get("secondSection_ConceptFive")
    data.secondSection_ConceptSix = request.json.get("secondSection_ConceptSix")
    db.session.add(data)
    db.session.commit()
    return 'data sended', 202

@app.route("/update_data_secondsection/<int:user>", methods=["PUT"])
def update_data_secondsection(user=None):
    if user is not None:
        print(user)
        data = Text_SecondSection.query.filter_by(user_id=user).all()
        data.secondSection_MainTitle = request.json.get("secondSection_MainTitle")
        data.secondSection_Description = request.json.get("secondSection_Description")
        data.secondSection_ConceptOne = request.json.get("secondSection_ConceptOne")
        data.secondSection_ConceptTwo = request.json.get("secondSection_ConceptTwo")
        data.secondSection_ConceptThree = request.json.get("secondSection_ConceptThree")
        data.secondSection_ConceptFour = request.json.get("secondSection_ConceptFour")
        data.secondSection_ConceptFive = request.json.get("secondSection_ConceptFive")
        data.secondSection_ConceptSix = request.json.get("secondSection_ConceptSix")
        db.session.commit()
        return 'data updated', 202

@app.route("/get_data_secondsection", methods=["GET"])
def get_data_secondsection():
        data = Text_SecondSection.query.all()
        serialize_list = list(map(lambda data: data.serialize(), data))
        response_body = {
            "msg":  "Get /data response was successful"
        }
        return jsonify(serialize_list), 201

@app.route("/data_secondsection/<int:user>", methods=["GET"])
def data_secondsection_byID(user=None):
        data = Text_SecondSection.query.filter_by(user_id=user).all()
        serialize_list = list(map(lambda data: data.serialize(), data))
        return jsonify(serialize_list), 201

## end of second section
## Start third section

@app.route("/send_data_thirdsection", methods=["POST"])
def send_data_thirdsection():
    data = Text_ThirdSection()
    data.id = request.json.get("id")
    data.user_id = request.json.get("user_id")
    data.thirdSection_MainTitle = request.json.get("thirdSection_MainTitle")
    data.thirdSection_Description = request.json.get("thirdSection_Description")
    data.thirdSection_LeftConceptOne_BlueHighlightText = request.json.get("thirdSection_LeftConceptOne_BlueHighlightText")
    data.thirdSection_LeftConceptOne_Title = request.json.get("thirdSection_LeftConceptOne_Title")
    data.thirdSection_LeftConceptOne_Description = request.json.get("thirdSection_LeftConceptOne_Description")
    data.thirdSection_RightConceptTwo_BlueHighlightText = request.json.get("thirdSection_RightConceptTwo_BlueHighlightText")
    data.thirdSection_RightConceptTwo_Title = request.json.get("thirdSection_RightConceptTwo_Title")
    data.thirdSection_RightConceptTwo_Description = request.json.get("thirdSection_RightConceptTwo_Description")
    data.thirdSection_LeftConceptThree_BlueHighlightText = request.json.get("thirdSection_LeftConceptThree_BlueHighlightText")
    data.thirdSection_LeftConceptThree_Title = request.json.get("thirdSection_LeftConceptThree_Title")
    data.thirdSection_LefttConceptThree_Description = request.json.get("thirdSection_LefttConceptThree_Description")
    db.session.add(data)
    db.session.commit()
    return 'data sended', 202

@app.route("/update_data_thirdsection/<int:user>", methods=["PUT"])
def update_data_thirdsection(user=None):
    if user is not None:
        print(user)
        data = Text_ThirdSection.query.filter_by(user_id=user).all()
        data.thirdSection_MainTitle = request.json.get("thirdSection_MainTitle")
        data.thirdSection_Description = request.json.get("thirdSection_Description")
        data.thirdSection_LeftConceptOne_BlueHighlightText = request.json.get("thirdSection_LeftConceptOne_BlueHighlightText")
        data.thirdSection_LeftConceptOne_Title = request.json.get("thirdSection_LeftConceptOne_Title")
        data.thirdSection_LeftConceptOne_Description = request.json.get("thirdSection_LeftConceptOne_Description")
        data.thirdSection_RightConceptTwo_BlueHighlightText = request.json.get("thirdSection_RightConceptTwo_BlueHighlightText")
        data.thirdSection_RightConceptTwo_Title = request.json.get("thirdSection_RightConceptTwo_Title")
        data.thirdSection_RightConceptTwo_Description = request.json.get("thirdSection_RightConceptTwo_Description")
        data.thirdSection_LeftConceptThree_BlueHighlightText = request.json.get("thirdSection_LeftConceptThree_BlueHighlightText")
        data.thirdSection_LeftConceptThree_Title = request.json.get("thirdSection_LeftConceptThree_Title")
        data.thirdSection_LefttConceptThree_Description = request.json.get("thirdSection_LefttConceptThree_Description")
        db.session.commit()
        return 'data updated', 202

@app.route("/get_data_thirdsection", methods=["GET"])
def get_data_thirdsection():
        data = Text_ThirdSection.query.all()
        serialize_list = list(map(lambda data: data.serialize(), data))
        response_body = {
            "msg":  "Get /data response was successful"
        }
        return jsonify(serialize_list), 201

@app.route("/data_thirdsection/<int:user>", methods=["GET"])
def data_thirdsection_byID(user=None):
        data = Text_ThirdSection.query.filter_by(user_id=user).all()
        serialize_list = list(map(lambda data: data.serialize(), data))
        return jsonify(serialize_list), 201

##End Third Section##
##Start of fourth Section##

@app.route("/send_data_fourthsection", methods=["POST"])
def send_data_fourthsection():
    data = Text_FourthSection()
    data.id = request.json.get("id")
    data.user_id = request.json.get("user_id")
    data.fourthSection_TestimonialsMainTitle = request.json.get("fourthSection_TestimonialsMainTitle")
    data.fourthSection_TestimonialsDescription = request.json.get("fourthSection_TestimonialsDescription")
    data.fourthSection_CardOneText = request.json.get("fourthSection_CardOneText")
    data.fourthSection_CardOne_Person = request.json.get("fourthSection_CardOne_Person")
    data.fourthSection_CardTwoText = request.json.get("fourthSection_CardTwoText")
    data.fourthSection_CardTwo_Person = request.json.get("fourthSection_CardTwo_Person")
    data.fourthSection_CardThreeText = request.json.get("fourthSection_CardThreeText")
    data.fourthSection_CardThree_Person = request.json.get("fourthSection_CardThree_Person")
    db.session.add(data)
    db.session.commit()
    return 'data sended', 202

@app.route("/update_data_fourthsection/<int:user>", methods=["PUT"])
def update_data_fourthsection(user=None):
    if user is not None:
        print(user)
        data = Text_FourthSection.query.filter_by(user_id=user).all()
        data.fourthSection_TestimonialsMainTitle = request.json.get("fourthSection_TestimonialsMainTitle")
        data.fourthSection_TestimonialsDescription = request.json.get("fourthSection_TestimonialsDescription")
        data.fourthSection_CardOneText = request.json.get("fourthSection_CardOneText")
        data.fourthSection_CardOne_Person = request.json.get("fourthSection_CardOne_Person")
        data.fourthSection_CardTwoText = request.json.get("fourthSection_CardTwoText")
        data.fourthSection_CardTwo_Person = request.json.get("fourthSection_CardTwo_Person")
        data.fourthSection_CardThreeText = request.json.get("fourthSection_CardThreeText")
        data.fourthSection_CardThree_Person = request.json.get("fourthSection_CardThree_Person")
        db.session.commit()
        return 'data updated', 202

@app.route("/get_data_fourthsection", methods=["GET"])
def get_data_fourthsection():
        data = Text_FourthSection.query.all()
        serialize_list = list(map(lambda data: data.serialize(), data))
        response_body = {
            "msg":  "Get /data response was successful"
        }
        return jsonify(serialize_list), 201

@app.route("/data_fourthsection/<int:user>", methods=["GET"])
def data_fourthsection_byID(user=None):
        data = Text_FourthSection.query.filter_by(user_id=user).all()
        serialize_list = list(map(lambda data: data.serialize(), data))
        return jsonify(serialize_list), 201

##END fourthsection##
##Start media endpoints##
@app.route("/send_data_media", methods=["POST"])
def send_data_media():
    data = Media()
    data.id = request.json.get("id")
    data.user_id = request.json.get("user_id")
    data.mainTitleVideo = request.json.get("mainTitleVideo")
    data.thirdSectionLeftConceptOneImg = request.json.get("thirdSectionLeftConceptOneImg")
    data.thirdSectionRightConceptTwoImg = request.json.get("thirdSectionRightConceptTwoImg")
    data.thirdSectionLeftConceptThreeImg = request.json.get("thirdSectionLeftConceptThreeImg")
    db.session.add(data)
    db.session.commit()
    return 'data sended', 202

@app.route("/update_data_media/<int:user>", methods=["PUT"])
def update_data_media(user=None):
    if user is not None:
        print(user)
        data = Media.query.filter_by(user_id=user).all()
        data.mainTitleVideo = request.json.get("mainTitleVideo")
        data.thirdSectionLeftConceptOneImg = request.json.get("thirdSectionLeftConceptOneImg")
        data.thirdSectionRightConceptTwoImg = request.json.get("thirdSectionRightConceptTwoImg")
        data.thirdSectionLeftConceptThreeImg = request.json.get("thirdSectionLeftConceptThreeImg")
        db.session.add(data)
        db.session.commit()
        return 'data updated', 202

@app.route("/get_data_media", methods=["GET"])
def get_data_media():
        data = Media.query.all()
        serialize_list = list(map(lambda data: data.serialize(), data))
        response_body = {
            "msg":  "Get /data response was successful"
        }
        return jsonify(serialize_list), 201

@app.route("/data_fourthsection/<int:user>", methods=["GET"])
def data_media_byID(user=None):
        data = Media.query.filter_by(user_id=user).all()
        serialize_list = list(map(lambda data: data.serialize(), data))
        return jsonify(serialize_list), 201

##End media endpoints##


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
