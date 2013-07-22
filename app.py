from flask import Flask, flash, render_template, session, url_for, request, redirect, g
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from forms import LoginForm
from flask.ext.openid import OpenID
import os
from flask.ext.login import login_user, logout_user, current_user, login_required, LoginManager
import unicodedata
import datetime

app = Flask(__name__)
app.secret_key = "some_"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

def str(x):
    return unicodedata.normalize('NFKD',x).encode('ascii','ignore')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(120), unique = False)
    school = db.Column(db.String(120), unique = False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(12), unique=False)
    skills = db.relationship('Skills',backref='user',lazy='dynamic')
    
    def is_authenticated(self):
        return True
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


    def __init__(self, username, email, password, name, school):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.school = school

    def __repr__(self):
        return "<User %r>" % self.username

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80))
    user1 = db.Column(db.String(80))
    user2 = db.Column(db.String(80))
    timestamp = db.Column(db.DateTime)
    messages = db.relationship('Message',backref='conversation',lazy='dynamic')

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


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.route("/")
def index():
    # return str(User.query.all()[0].password) # I don't think this will 
    
    return render_template("index.html")
@app.route("/signup")
def signup():
    return render_template("new.html")

@app.route("/results", methods=["POST"])
def results():
    error = None
    theUser = request.form["username"]
    email = request.form["email"]
    skill = request.form.getlist('skills')
    for users in User.query.all():
        if theUser == users.username:
            error = "already a username"

        if email == users.email:
            error= "already a registered email"

    try:
        x = User(theUser, email, request.form["password"], request.form["name"], request.form["school"])
        db.session.add(x)
        try :
            db.session.commit()
            for s in skill:
                S = Skills(skill=s,user=x)
                db.session.add(S)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return "broken"
        except Exception as e:
            db.session.rollback()
            return "broken"
            
        
    except IntegrityError:
        print "Not Working"
    string = unicodedata.normalize('NFKD',x.username).encode('ascii','ignore')
   
    return string #render_template("results.html", user=User.query.all(), error = error)

@app.route('/signin', methods = ["GET"])
def signin():
    return render_template("signin.html")

@app.route('/login', methods = ["GET","POST"])
def login():
    form = LoginForm()
    theUser = request.form["username"]
    password = request.form["password"]
    for users in User.query.all():
        if theUser == users.username:
            if password == users.password:
                user = load_user(users.id)
                login_user(user)
                flash('Logged ' + theUser + ' in successfully.')
                return redirect('/settings/'+theUser)
            else: return "Invalid Password!"        
    return "Invalid Username!!!"
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect('/')

@app.route("/settings/<username>")
@login_required
def settings(username):
    cS = []
    cR = []
    s = []
    user = User.query.filter_by(username=username).first()
    skill = user.skills.all()
    conversationsS = Conversation.query.filter_by(user1=unicodedata.normalize('NFKD',user.username).encode('ascii','ignore')).all()
    conversationsR = Conversation.query.filter_by(user2=unicodedata.normalize('NFKD',user.username).encode('ascii','ignore')).all()
    for c in conversationsS:
        cS.append({'user': str(c.user2), 'subject': str(c.subject), 'timestamp': c.timestamp, 'id': c.id})
    for c in conversationsR:
        cR.append({'user': str(c.user1), 'subject': str(c.subject), 'timestamp': c.timestamp, 'id': c.id})
    for SKILLS in skill:
        s.append(unicodedata.normalize('NFKD',SKILLS.skill).encode('ascii','ignore'))
    return render_template("settings.html",username=username,s=s,cS=cS,cR=cR)

@app.route("/conversation/<ID>/<user>")
@login_required
def conversation(ID,user):
    c = Conversation.query.get(ID)
    subject = str(c.subject)
    m=[]
    messages = c.messages.all()
    for M in messages:
        m.append({'sender':str(M.sender),'body':str(M.body),'timestamp':M.timestamp})
    return render_template("conversation.html",m=m,user=user,subject=subject,ID=ID)

@app.route("/reply/<ID>/<user>",methods=["GET"])
@login_required
def reply(ID,user):
    c = Conversation.query.get(ID)
    subject = str(c.subject)

    return render_template("reply.html",ID=ID,user=user)

@app.route("/replying",methods=["GET","POST"])
@login_required
def replying():
    ID = request.form['conversation']
    Body = request.form['body']
    user = request.form['user']
    c = Conversation.query.get(ID)
    if str(c.user2) == user: Sender = str(c.user1)
    else: Sender = str(c.user2)
    m = Message(sender=Sender,body=Body,timestamp=datetime.datetime.utcnow(),conversation=c)
    db.session.add(m)
    try:
        db.session.commit()
    except Exception as e:
            db.session.rollback()
            return "brokenm"
    return redirect('settings/'+Sender)
        

@app.route("/start",methods=["GET","POST"])
@login_required
def start():
    Sender = request.form["user"];
    Receiver = request.form["to"]
    if User.query.filter_by(username=Receiver).first() == None: return "Invalid User!"
    Subject = request.form["subject"]
    body = request.form["body"]
    c =  Conversation(subject=Subject,user1=Sender,user2=Receiver,timestamp=datetime.datetime.utcnow())
    db.session.add(c)
    try :
        db.session.commit()
        m  = Message(sender=Sender,body=body,timestamp=datetime.datetime.utcnow(),conversation=c)
        db.session.add(m)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return "brokenm"         
    except Exception as e:
        db.session.rollback()
        return "brokenc" 
    
    return redirect('/settings/'+Sender)



@app.route("/converse/<username>",methods=["GET"])
@login_required
def converse(username):
    return render_template("compose.html",username=username)


if __name__ == "__main__":
    db.session.rollback()
    db.create_all()

    # try:
    #     x = User("test3", "test2@gmail.com", "password")
    #     db.session.add(x)
    #     db.session.commit()
    #     print "worked"
    # except IntegrityError:
    #     print "Not Working"
    app.run(debug=True)
