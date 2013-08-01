from flask import Flask, flash, render_template, session, url_for, request, redirect, g
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from forms import LoginForm
from flask.ext.openid import OpenID
import os
from flask.ext.login import login_user, logout_user, current_user, login_required, LoginManager
import unicodedata
import urllib, hashlib
import datetime, operator

app = Flask(__name__)
app.secret_key = "some_"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
loggedUser =  None
curID = None
def uni(x):
    return unicodedata.normalize('NFKD',x).encode('ascii','ignore')

def uniquifyo(xl):
    final = []
    ranked = {}
    for x in xl:
        if x in ranked:
            ranked[x] += 1
            continue
        ranked[x] = 1
    sorted_x = sorted(ranked.iteritems(), key=operator.itemgetter(1),reverse=True)
    for y in sorted_x:
        final.append(y[0])
    return final
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
        self.first = first_name
        self.last = last_name
        self.password_description = password_description
        self.grad_year = grad_year
        self.major = major

    def get_role(self):
        return self.role

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

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.route("/")
def index():
    # return str(User.query.all()[0].password) # I don't think this will 
    
    return render_template("index.html", logged = loggedUser)

@app.route("/signup")
def signup():
    if loggedUser:
        return redirect("/")
    return render_template("signup.html")

@app.route("/signup/college",  methods=["POST", "GET"])
def collegesignup():
    if loggedUser:
        return redirect("/")
    if request.method == "POST":
        error = None
        theUser = request.form["username"].lower()
        email = request.form["email"].lower()
        skill = request.form.getlist('skills')
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        school = request.form["school"]
        year = request.form["year"]
        major = request.form["major"]
        password = request.form["password"]
        description = request.form["description"]

        
        c1 = request.form["company1"]
        t1 = request.form["title1"]
        experience1 = request.form["expDescription1"]

        # c2 = request.form["company2"]
        # c3 = request.form["company3"]

        
        # t2 = request.form["title2"]
        # t3 = request.form["title3"]


        # s1 = request.form["startdate1"]
        
        # s2 = request.form["startdate2"]
        # s3 = request.form["startdate3"]

        # e1 = request.form["enddate1"]
        # e2 = request.form["enddate2"]
        # e3 = request.form["enddate3"]

      
        for users in User.query.all():
            if theUser == users.username:
                error = "already a username"
                return render_template("new.html", error= error)
            if email == users.email:
                error= "already a registered email"
                return render_template("new.html", error= error)

        for item in [theUser, first_name, last_name, email, school, year, major, password, c1, t1]:
            if item == None or item == "":
                return render_template("new.html", error = "You failed to fill in a required field" + uni(item))
        try:
            x = User(theUser, first_name, last_name, email, password,description, school, year, major, "developer")
            db.session.add(x)
            try :
                db.session.commit()
                for s in skill:
                    S = Skills(skill=s,user=x)
                    db.session.add(S)
                
                try:
                    db.session.commit()

                    # for i in range(1,4):
                    #     if t[i] != "":
                    #         E = Experience(t[i], c[i], s[i], e[i], x)
                    #         db.session.add(E)
                    E = Experience(t1, c1, experience1, x)
                    db.session.add(E)
                    try:
                        db.session.commit()
                    except:
                        db.session.rollback()
                        return "couldn't commit experience"
                except Exception as e:
                    db.session.rollback()
                    return "couldn't commit skills or experience"
            except Exception as e:
                db.session.rollback()
                return "couldn't commit main"
                
            
        except IntegrityError:
            print "Not Working"
        string = unicodedata.normalize('NFKD',x.username).encode('ascii','ignore')
       
        return redirect("/signin")

    return render_template("new.html")


@app.route('/signin', methods = ["GET", "POST"])
def signin():
    if loggedUser:
            return redirect('/settings/'+ loggedUser.username.encode("utf-8"))
    if request.method == "POST":

        error = None
        form = LoginForm()
        theUser = request.form["username"].lower()
        password = request.form["password"].lower()
        print theUser
        for users in User.query.all():
            error = None
            if theUser == users.email:

                if password == users.password:
                    curID = users.id
                    global loggedUser
                    loggedUser = users

                    user = load_user(users.id)
                    login_user(user)
                    flash('Logged ' + theUser + ' in successfully.')
                    return redirect('/settings/'+ users.username)
                else: 
                    error = "Invalid username and password combination." 
                    return render_template("signin.html", error = error)     
        error = "Invalid username and password combination."
        return render_template("signin.html", error = error) 
    return render_template("signin.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    global loggedUser
    loggedUser = None
    return redirect('/')

@app.route("/settings/<username>")
@login_required
def settings(username):
    if loggedUser == None:
        return redirect("/signin")
    if username == loggedUser.username.encode("utf-8"):
        if User.query.get(current_user.get_id()).role == "developer":
            cS = []
            cR = []
            s = []
            exp =[]
            user = User.query.filter_by(username=username).first()
            email = user.email.encode("utf-8").lower()
            size = 150
            default = "http://www.blackdogeducation.com/wp-content/uploads/facebook-default-photo.jpg"

            gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest()
            gravatar_url += urllib.urlencode({'d':default, 's':str(size)})


            skill = user.skills.all()
            conversationsS = Conversation.query.filter_by(user1=unicodedata.normalize('NFKD',user.username).encode('ascii','ignore')).all()
            conversationsR = Conversation.query.filter_by(user2=unicodedata.normalize('NFKD',user.username).encode('ascii','ignore')).all()
            experience = user.experience.all()
            for c in conversationsS:
                cS.append({'user': uni(c.user2), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
            for c in conversationsR:
                cR.append({'user': uni(c.user1), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
            for SKILLS in skill:
                s.append(unicodedata.normalize('NFKD',SKILLS.skill).encode('ascii','ignore'))
            for exper in experience:
                exp.append({"title" : exper.title.encode("utf-8"), "company" : exper.company.encode("utf-8"), "description" : exper.description.encode("utf-8")})
            return render_template("settings.html",username=username,s=s,cS=cS,cR=cR, experience = exp, profpic = gravatar_url)
        else:
            cS = []
            cR = []
            s = []
            user = User.query.filter_by(username=username).first()

            conversationsS = Conversation.query.filter_by(user1=unicodedata.normalize('NFKD',user.username).encode('ascii','ignore')).all()
            conversationsR = Conversation.query.filter_by(user2=unicodedata.normalize('NFKD',user.username).encode('ascii','ignore')).all()
            for c in conversationsS:
                cS.append({'user': uni(c.user2), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
            for c in conversationsR:
                cR.append({'user': uni(c.user1), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
            user = User.query.filter_by(username=username).first()

            return render_template("company-settings.html",username=username,s=s,cS=cS,cR=cR)
    else:
        return "Can't acces this page"
@app.route("/conversation/<ID>/<user>")
@login_required
def conversation(ID,user):
    c = Conversation.query.get(ID)
    subject = uni(c.subject)
    m=[]
    messages = c.messages.all()
    for M in messages:
        m.append({'sender':uni(M.sender),'body':uni(M.body),'timestamp':M.timestamp})
    return render_template("conversation.html",m=m,user=user,subject=subject,ID=ID)

@app.route("/reply/<ID>/<user>",methods=["GET"])
@login_required
def reply(ID,user):
    c = Conversation.query.get(ID)
    subject = uni(c.subject)

    return render_template("reply.html",ID=ID,user=user)

@app.route("/replying",methods=["GET","POST"])
@login_required
def replying():
    ID = request.form['conversation']
    Body = request.form['body']
    user = request.form['user']
    c = Conversation.query.get(ID)
    if uni(c.user2) == user: Sender = uni(c.user1)
    else: Sender = uni(c.user2)
    m = Message(sender=Sender,body=Body,timestamp=datetime.datetime.utcnow(),conversation=c)
    db.session.add(m)
    try:
        db.session.commit()
    except Exception as e:
            db.session.rollback()
            return "brokenm"
    return redirect('settings/'+Sender)
        
@app.route("/search",methods=["GET","POST"])
def search():
    schools = []
    users = User.query.all()
    for user in users:
        if uni(user.school) == "" : continue
        schools.append(uni(user.school))
    schools = list(set(schools))
    return render_template('search.html',schools=schools)

@app.route("/sresults",methods=["GET","POST"])
def sresults():
    schools= request.form.getlist("schools")
    skills = request.form.getlist('skills')
    users = []
    
    for sch in schools:
        users += User.query.filter_by(school=sch).all()
    for sk in skills:
        skillList = Skills.query.filter_by(skill=sk).all()
        for s in skillList:
            users.append(s.user)

    users = uniquifyo(users)
    names = []
    for user in users:
        names.append(uni(user.username))
    return render_template('sresults.html',names=names)


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
@app.route("/profile/<username>")
@login_required 
def profile(username):

    if User.query.get(current_user.get_id()).role == "developer":

        cS = []
        cR = []
        s = []
        exp = []
        user = User.query.filter_by(username=username).first()
        skill = user.skills.all()
        experience = user.experience.all()
        for SKILLS in skill:
            s.append(unicodedata.normalize('NFKD',SKILLS.skill).encode('ascii','ignore'))
        for exper in experience:
            exp.append({"title" : exper.title.encode("utf-8"), "company" : exper.company.encode("utf-8"), "company" : exper.company.encode("utf-8")})


        return render_template("profile.html",user = user, username=username,s=s, experience = exp)
    else:
        return "not setup yet"


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
