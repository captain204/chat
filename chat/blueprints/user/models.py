from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from chat.extensions import db
from datetime import datetime

class User(UserMixin, db.Model):
    """User Model """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(250), unique=True, nullable=False)
    messages = db.relationship('Message', backref=db.backref('messages',lazy=True))
    friends = db.relationship('Friend',backref=db.backref('friends',lazy=True))
    created_on = db.Column(db.DateTime,default=datetime.utcnow)
    

    def set_password(self,password):
        """Create User Password """
        self.password = generate_password_hash(password,method='sha256')

    def check_password(self,password):
        """Check Hashed Password"""
        return check_password_hash(self.password,password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Message(db.Model):
    """Messages model"""
    __tablename__ ='messages'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    body = db.Column(db.Text,nullable=False)
    status = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime,  default=datetime.utcnow)


    def __repr__(self):
        return '<Message {}>'.format(self.id)


class Friend(db.Model):
    """Friends model """
    __tablename__ = 'friends'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    friends_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Friend {}>'.format(self.id)

    