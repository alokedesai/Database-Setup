from app import app, login_manager, loggedUser, db
from flask import Flask, flash, render_template, session, url_for, request, redirect, g, send_from_directory
from flask.ext.login import login_user, logout_user, current_user, login_required
from models import User,Skills,File,Experience,Conversation,Message,Ratings
from forms import LoginForm
import urllib, hashlib
from config import ALLOWED_EXTENSIONS
from werkzeug import secure_filename
import os
import datetime, operator
import unicodedata

def rating(x):
    total = 0
    for y in x:
        total += y.stars
    total = total/len(x)
    return total
def to_int(x):
    return int(x)
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
            R = []
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
            conversations = user.conversations.all() + user.conversations2.all()
            experience = user.experience.all()
            ratings = user.rated.all()
            if len(ratings) > 0:
                avg = rating(ratings)
            else:
                avg = 0
            for r in ratings:
                R.append({'rater': uni(r.rated.username), 'stars': r.stars, 'review': r.review, 'id': r.id})
            for c in conversations:
                if c.user.username == username:
                    cS.append({'user': uni(c.user2.username), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
                else:
                    cS.append({'user': uni(c.user.username), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
           
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
            return render_template("settings.html",username=username,s=s,cS=cS,review=R,avg=avg, experience = exp, profpic = gravatar_url, files = files, logged = loggedUser, year = uni(loggedUser.grad_year), major = major, school = school, first = loggedUser.first_name.encode("utf-8"), last = loggedUser.last_name.encode("utf-8"), curUsername = username)
        else:
            cS = []
            s = []
            user = User.query.filter_by(username=username).first()
            
            conversations = user.conversations.all()+user.conversations2.all()
            experience = user.experience.all()
            for c in conversations:
                if c.user.username == username:
                    cS.append({'user': uni(c.user2.username), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
                else:
                    cS.append({'user': uni(c.user.username), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
            user = User.query.filter_by(username=username).first()

            return render_template("company-settings.html",username=username,s=s,cS=cS)
    else:
        return redirect("/")

@app.route("/rating/ID/<ID>")
@login_required
def rating_id(ID):
    r = Ratings.query.get(ID)
    R = []
    R.append({'stars':r.stars,'rated':uni(r.rated.username),'rater':uni(r.rater.username),'review':r.review})
    return render_template("ratings.html",rated=uni(r.rated.username),R=R)

@app.route("/rating/<user>")
def rating_user(user):
    user = User.query.filter_by(username=user).first()
    

    r = user.rated.all()
    if len(r) == 0:
        R = None
    user = uni(user.username)
    R = []
    for rating in r:
        R.append({'stars':rating.stars,'rated':uni(rating.rated.username),'rater':uni(rating.rater.username),'review':rating.review})
    return render_template("ratings.html",rated=user,R=R)

@app.route("/rate/<user>", methods=["GET", "POST"])
@login_required
def rate(user):
    error = None
    global loggedUser
    logged = loggedUser


    # redirect to homepage if not logged in
    if logged == None:
        return redirect("/")


    #get the user who is to be rated based on the url
    user = User.query.filter_by(username=user).first()

 
    first = uni(user.first_name)
    email = uni(user.email)

    #gravatar code for picture
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest()
    gravatar_url += "?" + "s=" + "150" +"&" + "d=" + "mm"
    
    if request.method == "POST":
        score = request.form["score"]
        if score == unicode(''):
            error =  "Please enter a star amount more than 0"
            return render_template("rate.html",logged = logged, image = gravatar_url, first = first, error = error)
        review = request.form["review"]

        if review == unicode(''):
            error = "Please enter a review"
            return render_template("rate.html",logged = logged, image = gravatar_url, first = first, error = error)
        rated = user

        Rater = loggedUser.username.encode('utf-8');
        rater = User.query.filter_by(username=Rater).first()

        #create ratings object from the data from the form. The rater is the user that is
        #currently logged in

        rating = Ratings(user, rater, score, review)

        #add and commit to database
        db.session.add(rating)
        db.session.commit()
        
        return redirect("/rating/" + user.username)
    
   


    return render_template("rate.html",logged = logged, image = gravatar_url, first = first, error = error)


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
    Sender = loggedUser.username.encode("utf-8")
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
        size = 200
        default = "http://www.blackdogeducation.com/wp-content/uploads/facebook-default-photo.jpg"

        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(uni(user.email).lower()).hexdigest()
            # gravatar_url += urllib.urlencode({'default':default, 's':str(size)})
        gravatar_url += "?" + "s=" + str(size) +"&" + "d=" + "mm"
        skills = user.skills.all()
        if skills > 3:
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
    Sender = loggedUser.username.encode('utf-8');
    sender = User.query.filter_by(username=Sender).first()
    Receiver = request.form["to"]
    if User.query.filter_by(username=Receiver).first() == None: return "Invalid User!"
    receiver = User.query.filter_by(username=Receiver).first()
    Subject = request.form["subject"]
    body = request.form["body"]
    c =  Conversation(sender,receiver,Subject)
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
    user = User.query.filter_by(username=username).first()

    return render_template("compose.html",username=username, first = uni(loggedUser.first_name), last = uni(loggedUser.last_name), to_first = uni(user.first_name), to_last = uni(user.last_name))


@app.route("/profile/<username>", methods=['GET', 'POST'])

def profile(username):
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

    #NOT WORKING-- redirect to the user's setting page if the user is trying to access their own profile       
    if loggedUser:
        cur_user = User.query.filter_by(username=loggedUser.username).first()
        if username == uni(cur_user.username):
            return redirect("/settings/" + username)

    user = User.query.filter_by(username=username).first() 

    #this needs to be updated to a normal 404 error. This happens when there is no user
    #with this username
    if user == None:
        return "404"
    if user.role == "developer":
        cS = []
        R = []
        s = []
        exp =[]
        f=[]
        
        email = user.email.encode("utf-8").lower()
        school = uni(user.school)
        major = uni(user.major)
        size = 200
        default = "http://www.blackdogeducation.com/wp-content/uploads/facebook-default-photo.jpg"

        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest()
        # gravatar_url += urllib.urlencode({'default':default, 's':str(size)})
        gravatar_url += "?" + "s=" + str(size) +"&" + "d=" + "mm"
        

        
        skill = user.skills.all()
        files = user.files.all()
        conversations = user.conversations.all() + user.conversations2.all()
        experience = user.experience.all()
        ratings = user.rated.all()
        if len(ratings) > 0:
            avg = rating(ratings)
        else:
            avg = 0
        for r in ratings:
            R.append({'rater': uni(r.rated.username), 'stars': r.stars, 'review': r.review, 'id': r.id})
        for c in conversations:
            if c.user.username == username:
                cS.append({'user': uni(c.user2.username), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
            else:
                cS.append({'user': uni(c.user.username), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
       
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
        return render_template("settings.html",username=username,s=s,cS=cS,review=R,avg=avg, experience = exp, profpic = gravatar_url, files = files, logged = loggedUser, year = uni(user.grad_year), major = major, school = school, first = user.first_name.encode("utf-8"), last = user.last_name.encode("utf-8"), curUsername = username)
    else:
        cS = []
        s = []
        user = User.query.filter_by(username=username).first()
        
        conversations = user.conversations.all()+user.conversations2.all()
        experience = user.experience.all()
        for c in conversations:
            if c.user.username == username:
                cS.append({'user': uni(c.user2.username), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
            else:
                cS.append({'user': uni(c.user.username), 'subject': uni(c.subject), 'timestamp': c.timestamp, 'id': c.id})
        user = User.query.filter_by(username=username).first()

        return render_template("company-settings.html",username=username,s=s,cS=cS)

#OLD PROFILE
# @app.route("/profile/<username>")
# @login_required 
# def profile(username):

#     if User.query.get(current_user.get_id()).role == "developer":

#         cS = []
#         cR = []
#         s = []
#         exp = []
#         user = User.query.filter_by(username=username).first()
#         skill = user.skills.all()
#         experience = user.experience.all()
#         files = user.files.all()
#         #files = files.filename.encode("utf-8")
#         files = "resume"
#         for SKILLS in skill:
#             s.append(SKILLS.skill.encode('utf-8'))
#         for exper in experience:
#             exp.append({"title" : exper.title.encode("utf-8"), "company" : exper.company.encode("utf-8"), "company" : exper.company.encode("utf-8")})


#         return render_template("profile.html",user = user, username=username,s=s, experience = exp, f =files)
#     else:
        return "not setup yet"
