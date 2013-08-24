from app import models,db

users = models.User.query.all()
a = models.Conversation(user=users[0],user2=users[1],extra_data="hi")
db.session.rollback()
db.session.add(a)
db.session.commit()

