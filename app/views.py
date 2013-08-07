from app import app, login_manager, loggedUser, db
from flask import Flask, flash, render_template, session, url_for, request, redirect, g, send_from_directory
from flask.ext.login import login_user, logout_user, current_user, login_required
from models import User,Skills,File,Experience,Conversation,Message
from forms import LoginForm
import urllib, hashlib
from config import ALLOWED_EXTENSIONS
from werkzeug import secure_filename
import os
import datetime, operator
import unicodedata

def uni(x):
    return x.encode('utf-8')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS


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
@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.route("/")
def index():
    # return str(User.query.all()[0].password) # I don't think this will 
    curUsername = None
    if loggedUser:
        curUsername = loggedUser.username.encode("utf-8")
    return render_template("index.html", logged = loggedUser, curUsername = curUsername)

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

                    E = Experience(t1, c1, experience1, x)
                    db.session.add(E)
                    try:
                        db.session.commit()

                        file = request.files['file']
                        if file and allowed_file(file.filename):
                            filename = secure_filename(str(x.id) + file.filename[file.filename.rfind("."):])
                            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                            f = File(filename=filename,user=x)
                            db.session.add(f)
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
        string = x.username.encode('utf-8')
       
        return redirect("/signin")
    ins = open("t1.txt")
    array = []
    for line in ins:
        x = line.replace("\n", "")
        if x[0].isalpha():
            x = x[0].upper() + x[1:]
        array.append(x)
    return render_template("new.html", options= array)



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






@app.route("/settings/<username>", methods=['GET', 'POST'])
@login_required
def settings(username):
    if request.method=='POST':
        file = request.files['file']
        u = User.query.filter_by(username=username).first()
        if file and allowed_file(file.filename):
            filename = secure_filename(str(loggedUser.id) + file.filename[file.filename.rfind("."):])
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            f = File(filename=filename,user=u)
            db.session.add(f)
            db.session.commit()
            return redirect("/settings/"+username)        
    if loggedUser == None:
        return redirect("/signin")
    if username == loggedUser.username.encode("utf-8"):
        if User.query.get(current_user.get_id()).role == "developer":
            cS = []
            cR = []
            s = []
            exp =[]
            f=[]
            user = User.query.filter_by(username=username).first()
            email = user.email.encode("utf-8").lower()
            school = uni(loggedUser.school)
            major = uni(loggedUser.major)
            size = 200
            default = "http://www.blackdogeducation.com/wp-content/uploads/facebook-default-photo.jpg"

            gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest()
            # gravatar_url += urllib.urlencode({'default':default, 's':str(size)})
            gravatar_url += "?" + "s=" + str(size) +"&" + "d=" + "mm"
            

            
            skill = user.skills.all()
            files = user.files.all()
            conversationsS = Conversation.query.filter_by(user1=unicodedata.normalize('NFKD',user.username).encode('ascii','ignore')).all()
            conversationsR = Conversation.query.filter_by(user2=unicodedata.normalize('NFKD',user.username).encode('ascii','ignore')).all()
            experience = user.experience.all()
            for c in conversationsS:
                cS.append({'user': uni(c.user2), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
            for c in conversationsR:
                cR.append({'user': uni(c.user1), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
            for SKILLS in skill:
                s.append(uni(SKILLS.skill))
            for fil in files:
                f.append(fil.filename.encode("utf-8"))
            if len(f) == 0:
                files = None
            else:
                files = f[0] 
            for exper in experience:
                exp.append({"title" : exper.title.encode("utf-8"), "company" : exper.company.encode("utf-8"), "description" : exper.description.encode("utf-8")})
            return render_template("settings.html",username=username,s=s,cS=cS,cR=cR, experience = exp, profpic = gravatar_url, files = files, logged = loggedUser, year = uni(loggedUser.grad_year), major = major, school = school, first = loggedUser.first_name.encode("utf-8"), last = loggedUser.last_name.encode("utf-8"), curUsername = username)
        else:
            cS = []
            cR = []
            s = []
            user = User.query.filter_by(username=username).first()

            conversationsS = Conversation.query.filter_by(user1=user.username.encode('utf-8'))
            conversationsR = Conversation.query.filter_by(user2=user.username.encode('utf-8'))
            for c in conversationsS:
                cS.append({'user': uni(c.user2), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
            for c in conversationsR:
                cR.append({'user': uni(c.user1), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
            user = User.query.filter_by(username=username).first()

            return render_template("company-settings.html",username=username,s=s,cS=cS,cR=cR)
    else:
        return redirect("/")
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
    skills = []
    users = User.query.all()
    for user in users:
        if uni(user.school) == "" : continue
        schools.append(uni(user.school))
        for x in user.skills.all():
            skills.append(uni(x.skill))
    skills = list(set(skills))
    schools = list(set(schools))
    curUsername = ""
    if loggedUser:
        curUsername = uni(loggedUser.username)
    
    return render_template('search.html',schools=schools, skills=  skills, logged = loggedUser, curUsername = curUsername)

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
        size = 80
        default = "http://www.blackdogeducation.com/wp-content/uploads/facebook-default-photo.jpg"

        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(uni(user.email).lower()).hexdigest()
            # gravatar_url += urllib.urlencode({'default':default, 's':str(size)})
        gravatar_url += "?" + "s=" + str(size) +"&" + "d=" + "mm"
        skills = user.skills.all()
        if skills >= 5:
            skills = skills[:3]
        skill = []
        for i in skills:
            skill.append(uni(i.skill))
        names.append({"username" : uni(user.username) , "name" : uni(user.first_name) + " " + uni(user.last_name), "school" : uni(user.school), "image" : gravatar_url, "skills" : skill})
    return render_template('sresults.html',names=names)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method=='POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(loggedUser.email.encode("utf-8") + file.filename[file.filename.rfind("."):])
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

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
        files = user.files.all()[0]
        files = files.filename.encode("utf-8")
        for SKILLS in skill:
            s.append(SKILLS.skill.encode('utf-8'))
        for exper in experience:
            exp.append({"title" : exper.title.encode("utf-8"), "company" : exper.company.encode("utf-8"), "company" : exper.company.encode("utf-8")})


        return render_template("profile.html",user = user, username=username,s=s, experience = exp, f =files)
    else:
        return "not setup yet"
