import app
from app import db

user = app.User.query.all()
for u in user:
    db.session.delete(u)
db.session.commit()

skill = app.Skills.query.all()
for s in skill:
    db.session.delete(s)
db.session.commit()


