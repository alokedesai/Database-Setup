from flask import Flask, flash, render_template, session, url_for, request, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask.ext.login import LoginManager, login_required

app = Flask(__name__)
app.secret_key = "some_"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test1.db"

db = SQLAlchemy(app)
login_manager = LoginManager

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(12), unique=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.username

@app.route("/")
def index():
    # return str(User.query.all()[0].password) # I don't think this will 
    return render_template("new.html")
@app.route("/results", methods=["POST"])
def results():
    error = None
    theUser = request.form["username"]
    email = request.form["email"]
    for users in User.query.all():
        if theUser == users.username:
            error = "already a username"
        if email == users.email:
            erorr= "already a registered email"

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
@app.route('/login', methods = ["POST", "GET"])
def login():
    theUser = request.form["username"]
    email = request.form["email"]
    for users in User.query.all():
        if theUser == users.username:
            
            if email == users.email:
                return url_for("index")
            else:
                 return "password didn't match"
    return render_template("login.html")

@app.route("/logged")
@login_required
def logged():
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

    app.run(debug=True)