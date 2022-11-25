from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, )
    password = db.Column(dbs.String(50), nullable=False)

class Media(db.Model):
    __tablename__ = "medias"
    id = db.Column(db.Integer, primary_key=True)
    user.id= db.Column(db.Integer, db.ForeignKey('users_id'), nullable=False)
    mainTitleVideo = db.Column(db.string(500))

class Text(db.Model):
    __tablename__ = "texts"
    id = db.Column(db.Integer, primary_key=True)
    user.id= db.Column(db.Integer, db.ForeignKey('users_id'), nullable=False)
    mainTitle = db.Column(db.string(200), nullable=False)
    mainDescription = db.Column(db.string(200))
    secondSectionMainTitle = db.Column(db.string(200), nullable=False)
    secondSectionDescription = db.Column(db.string(200))
