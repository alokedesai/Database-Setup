from flask import Flask, flash, render_template, session, url_for, request, redirect, g
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from forms import LoginForm
from flask.ext.openid import OpenID
import os
import flask.ext.login

app = Flask(__name__)
app.secret_key = "some_"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test1.db"

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(12), unique=False)
    
    def is_authenticated(self):
        return True
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.username

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.route("/")
def index():
    # return str(User.query.all()[0].password) # I don't think this will 
    
    return render_template("new.html",user=user)

@app.route("/results", methods=["POST"])
def results():
    error = None
    theUser = request.form["username"]
    email = request.form["email"]
    for users in User.query.all():
        if theUser == users.username:
            error = "already a username"
        if email == users.email:
            error= "already a registered email"

    try:
        x = User(theUser, email, request.form["password"])
        db.session.add(x)
        try :
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            
        
    except IntegrityError:
        print "Not Working"

   
    return render_template("results.html", user=User.query.all(), error = error)

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
                flash("Logged in successfully.")
                return render_template("results.html")
            else: return "Invalid Password!"        
    return "Invalid Username!!!"
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route("/settings")
@login_required
def settings():
    return "yay"
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

    app.run()
