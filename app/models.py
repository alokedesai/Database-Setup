from app import db
from app import app
import re

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(120), unique = False)
    last_name = db.Column(db.String(120), unique = False)
    school = db.Column(db.String(120), unique = False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(12), unique=False)
    password_description = db.Column(db.String(200), unique=False)
    grad_year = db.Column(db.String(4), unique=False)
    major = db.Column(db.String(120), unique=False)
    role = db.Column(db.String(80), unique=False)
    skills = db.relationship('Skills',backref='user',lazy='dynamic')
    experience  = db.relationship("Experience", backref='user',lazy='dynamic')
    files = db.relationship('File',backref='user',lazy='dynamic')
    conversation = db.relationship('Conversation',backref='user',lazy='dynamic')
    
    def is_authenticated(self):
        return True
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
    

    def __init__(self, username, first_name, last_name, email, password, password_description, school, grad_year, major, role):
        self.username = username
        self.email = email
        self.password = password
        self.school = school
        self.role = role
        self.first_name = first_name
        self.last_name = last_name
        self.password_description = password_description
        self.grad_year = grad_year
        self.major = major

    def get_role(self):
        return self.role

    def __repr__(self):
        return "<User %r>" % self.username

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<File %r>" % self.filename
    
class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80))
    user1 = db.Column(db.Integer, db.ForeignKey("user.id"))
    user2 = db.Column(db.Integer, db.ForeignKey("user.id"))
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return "<Conversation %r>" % self.subject
	
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'))

    def __repr__(self):
        return "<Message %r>" % self.sender

    
class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Skill %r>" % self.skill
class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    company = db.Column(db.String(80))
    description = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, company, description, user):
        self.title = title
        self.company = company
        self.description = description
       
        self.user = user

    def __repr__(self):
        return "<Experience %r>" % self.title
