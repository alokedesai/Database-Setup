from app import db, Skills,User
import random

skills = ["Java", "JavaScript","C","C++","PHP","HTML","CSS","Ruby","Python","Objective C"]
users = User.query.all()

for u in users:
    rskills = skills[:]
    x = random.randint(1,8)
    for y in range(x):
        sk = random.choice(rskills)
        rskills.remove(sk)
        s = Skills(skill=sk,user=u)
        db.session.add(s)
db.session.commit()
