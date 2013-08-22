from app import db
from app import app
import re,datetime

class Conversation(db.Model):
    __tablename__='conversation'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',foreign_keys=[user_id],
        backref=db.backref('conversations', lazy='dynamic'))
    user2_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user2 = db.relationship('User',foreign_keys=[user2_id],
                            backref=db.backref('conversations2',lazy='dynamic'))
    subject = db.Column(db.String(50),unique=False)
    timestamp = db.Column(db.DateTime)
    
    def __init__(self, user, user2, subject):
        self.user = user
        self.user2 = user2
        self.subject = subject
        self.timestamp = datetime.datetime.utcnow()

class User(db.Model):
    __tablename__='user'
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
   #all_conversations = db.relationship('Conversation',
    #    primaryjoin='or_(User.id == Conversation.user1_id, User.id == ' \
    #    'Conversation.user2_id)', lazy='dynamic')
    # Replies where this is this user.
    #replies = db.relationship("Reply", backref="user")
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
    
#class Conversation(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    user1_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#    user2_id = db.Column(db.Integer, db.ForeignKey("user.id"))        
#    user1 = db.relationship('User', foreign_keys=[user1_id], 
#        backref='conversations_as_user1')       
#    user2 = db.relationship('User', foreign_keys=[user2_id], 
#        backref='conversations_as_user2')
#    # Replies to this conversation.
#    replies = db.relationship("Reply", backref="conversation")
#   
#    def __init__(self,user1, user2):
#        self.user1 = user1
#        self.user2 = user2
#            
#        
#    def __repr__(self):
#        return "<Conversation %r>" % self.user1
#class Reply(db.Model):
#    id = db.Column(db.Integer, primary_key = True)
#    reply = db.Column(db.Text)
#    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#    conversation_id = db.Column(db.Integer, db.ForeignKey("conversation.id"))
#
#    def __init__(self, reply,user_id, time):
#        self.reply = reply
#        self.user_id = user_id
#        self.time = time
#    def __repr__(self):
#        return "<Reply %r>" % self.reply

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'))
    conversation = db.relationship("Conversation", backref=db.backref("messages",lazy="dynamic"))
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
