from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=False)
    email = db.Column(db.String(100), nullable=False, unique=True )
    password = db.Column(db.String(50), nullable=False, unique=False)
    is_active = db.Column(db.Boolean(), nullable=False, unique=False)

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
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mainTitleVideo = db.Column(db.String(500))
    thirdSectionLeftConceptOneImg = db.Column(db.String(500))
    thirdSectionRightConceptTwoImg = db.Column(db.String(500))
    thirdSectionLeftConceptThreeImg = db.Column(db.String(500))


class Text(db.Model):
    __tablename__ = "text"
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    mainTitle = db.Column(db.String(200), nullable=False)
    mainDescription = db.Column(db.String(200))

    secondSection_MainTitle = db.Column(db.String(200), nullable=False)
    secondSection_Description = db.Column(db.String(200))
    secondSection_ConceptOne = db.Column(db.String(200))
    secondSection_ConceptTwo = db.Column(db.String(200))
    secondSection_ConceptThree = db.Column(db.String(200))
    secondSection_ConceptFour = db.Column(db.String(200))
    secondSection_ConceptFive = db.Column(db.String(200))
    secondSection_ConceptSix = db.Column(db.String(200))

    thirdSection_MainTitle = db.Column(db.String(200), nullable=False)
    thirdSection_Description = db.Column(db.String(200))
    thirdSection_LeftConceptOne_BlueHighlightText = db.Column(db.String(200))
    thirdSection_LeftConceptOne_Title = db.Column(db.String(200))
    thirdSection_LeftConceptOne_Description = db.Column(db.String(200))
    thirdSection_RightConceptTwo_BlueHighlightText = db.Column(db.String(200))
    thirdSection_RightConceptTwo_Title = db.Column(db.String(200))     
    thirdSection_RightConceptTwo_Description = db.Column(db.String(200))
    thirdSection_LeftConceptThree_BlueHighlightText = db.Column(db.String(200))
    thirdSection_LeftConceptThree_Title = db.Column(db.String(200))
    thirdSection_LefttConceptThree_Description = db.Column(db.String(200))

    fourthSection_TestimonialsMainTitle = db.Column(db.String(200), nullable=False)
    fourthSection_TestimonialsDescription = db.Column(db.String(200))
    fourthSection_CardOneText = db.Column(db.String(200))
    fourthSection_CardOne_Person = db.Column(db.String(200))
    fourthSection_CardTwoText = db.Column(db.String(200))
    fourthSection_CardTwo_Person = db.Column(db.String(200))
    fourthSection_CardThreeText = db.Column(db.String(200))
    fourthSection_CardThree_Person = db.Column(db.String(200))

