from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False, unique=False)
    is_active = db.Column(db.Boolean(), default=True, nullable=False, unique=False)
    
    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "is_active": self.is_active
        }


class Media(db.Model):
    __tablename__ = "media"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    mainTitleVideo = db.Column(db.String(500))
    thirdSectionLeftConceptOneImg = db.Column(db.String(), unique=True)
    thirdSectionRightConceptTwoImg = db.Column(db.String(), unique=True)
    thirdSectionLeftConceptThreeImg = db.Column(db.String(), unique=True)

    def __repr__(self):
        return '<User %r>' % self.user_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "mainTitleVideo": self.mainTitleVideo,
            "thirdSectionLeftConceptOneImg": self.thirdSectionLeftConceptOneImg,
            "thirdSectionRightConceptTwoImg" : self.thirdSectionRightConceptTwoImg,
            "thirdSectionLeftConceptThreeImg": self. thirdSectionLeftConceptThreeImg
        }


class Text_FirstSection(db.Model):
    __tablename__ = "text_firstsection"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mainTitle = db.Column(db.String(200), unique=True)
    mainDescription = db.Column(db.String(200), unique=True)

    def __repr__(self):
        return '<Text_FirstSection %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "mainTitle": self.mainTitle,
            "mainDescription": self.mainDescription
        }


class Text_SecondSection(db.Model):
    __tablename__ = "text_secondsection"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    secondSection_MainTitle = db.Column(db.String(200), unique=True)
    secondSection_Description = db.Column(db.String(200), unique=True)
    secondSection_ConceptOne = db.Column(db.String(200), unique=True)
    secondSection_ConceptTwo = db.Column(db.String(200), unique=True)
    secondSection_ConceptThree = db.Column(db.String(200), unique=True)
    secondSection_ConceptFour = db.Column(db.String(200), unique=True)
    secondSection_ConceptFive = db.Column(db.String(200), unique=True)
    secondSection_ConceptSix = db.Column(db.String(200), unique=True)

    def __repr__(self):
        return '<Text_SecondSection %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "secondSection_MainTitle": self.secondSection_MainTitle,
            "secondSection_Description": self.secondSection_Description,
            "secondSection_ConceptOne": self.secondSection_ConceptOne,
            "secondSection_ConceptTwo": self.secondSection_ConceptTwo,
            "secondSection_ConceptThree": self.secondSection_ConceptThree,
            "secondSection_ConceptFour": self.secondSection_ConceptFour,
            "secondSection_ConceptFive": self.secondSection_ConceptFive,
            "secondSection_ConceptSix": self.secondSection_ConceptSix
        }

class Text_ThirdSection(db.Model):
    __tablename__ = "text_thirdsection"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    thirdSection_MainTitle = db.Column(db.String(200), unique=True)
    thirdSection_Description = db.Column(db.String(200), unique=True)
    thirdSection_LeftConceptOne_BlueHighlightText = db.Column(db.String(200), unique=True)
    thirdSection_LeftConceptOne_Title = db.Column(db.String(200), unique=True)
    thirdSection_LeftConceptOne_Description = db.Column(db.String(200), unique=True)
    thirdSection_RightConceptTwo_BlueHighlightText = db.Column(db.String(200), unique=True)
    thirdSection_RightConceptTwo_Title = db.Column(db.String(200), unique=True)
    thirdSection_RightConceptTwo_Description = db.Column(db.String(200), unique=True)
    thirdSection_LeftConceptThree_BlueHighlightText = db.Column(db.String(200), unique=True)
    thirdSection_LeftConceptThree_Title = db.Column(db.String(200), unique=True)
    thirdSection_LefttConceptThree_Description = db.Column(db.String(200), unique=True)

    def __repr__(self):
        return '<User %r>' % self.user_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "thirdSection_MainTitle": self.thirdSection_MainTitle,
            "thirdSection_Description": self.thirdSection_Description,
            "thirdSection_LeftConceptOne_BlueHighlightText": self.thirdSection_LeftConceptOne_BlueHighlightText,
            "thirdSection_LeftConceptOne_Title": self.thirdSection_LeftConceptOne_Title,
            "thirdSection_LeftConceptOne_Description": self.thirdSection_LeftConceptOne_Description,
            "thirdSection_RightConceptTwo_BlueHighlightText": self.thirdSection_RightConceptTwo_BlueHighlightText,
            "thirdSection_RightConceptTwo_Title": self.thirdSection_RightConceptTwo_Title,
            "thirdSection_RightConceptTwo_Description": self.thirdSection_RightConceptTwo_Description,
            "thirdSection_LeftConceptThree_BlueHighlightText": self.thirdSection_LeftConceptThree_BlueHighlightText,
            "thirdSection_LeftConceptThree_Title": self.thirdSection_LeftConceptThree_Title,
            "thirdSection_LefttConceptThree_Description": self.thirdSection_LefttConceptThree_Description
        }

class Text_FourthSection(db.Model):
    __tablename__ = "text_fourthsection"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    fourthSection_TestimonialsMainTitle =db.Column(db.String(200), unique=True)
    fourthSection_TestimonialsDescription = db.Column(db.String(200), unique=True)
    fourthSection_CardOneText = db.Column(db.String(200), unique=True)
    fourthSection_CardOne_Person = db.Column(db.String(200), unique=True)
    fourthSection_CardTwoText = db.Column(db.String(200), unique=True)
    fourthSection_CardTwo_Person = db.Column(db.String(200), unique=True)
    fourthSection_CardThreeText = db.Column(db.String(200), unique=True)
    fourthSection_CardThree_Person = db.Column(db.String(200), unique=True)

    def __repr__(self):
        return '<User %r>' % self.user_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "fourthSection_TestimonialsMainTitle": self.fourthSection_TestimonialsMainTitle,
            "fourthSection_TestimonialsDescription": self.fourthSection_TestimonialsDescription,
            "fourthSection_CardOneText": self.fourthSection_CardOneText,
            "fourthSection_CardOne_Person": self.fourthSection_CardOne_Person,
            "fourthSection_CardTwoText": self.fourthSection_CardTwoText,
            "fourthSection_CardTwo_Person": self.fourthSection_CardTwo_Person,
            "fourthSection_CardThreeText": self.fourthSection_CardThreeText,
            "fourthSection_CardThree_Person": self.fourthSection_CardThree_Person
        }   