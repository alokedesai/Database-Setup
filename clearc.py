from app import Conversation, db, Message

conversation = Conversation.query.all()
for c in conversation:
    db.session.delete(c)
message = Message.query.all()
for m in message:
    db.session.delete(m)
db.session.commit()
