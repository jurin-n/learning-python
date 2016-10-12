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
        return '<User id=%r,username=%r,email=%r>' % self.id % self.username % self.email
        # user_dict = {}
        # user_dict['id'] = self.id
        # user_dict['username'] = self.username
        # user_dict['email'] = self.email
        # return user_dict

    def user_dict(self):
        user_dict = {}
        user_dict['id'] = self.id
        user_dict['username'] = self.username
        user_dict['email'] = self.email
        return user_dict

def get_user(id):
    return User.query.filter_by(id=id).first()

def add_user(username,email):
    admin = User(username,email)

    db.session.add(admin)
    db.session.commit()

    return
