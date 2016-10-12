from factory import db
import uuid

class User(db.Model):
    id = db.Column(db.String(256), primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.id = str(uuid.uuid4())
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.id
