from flask import Blueprint, request
import json
from models import User
from factory import db

resource = Blueprint('users_app', __name__)

@resource.route('/<id>', methods=['GET'])
def get_user(id):
    return 'Hello ID=' + id + ' User!!!!!!!!!'

@resource.route('/', methods=['POST'])
def post_user():
    request_body = request.get_json(force=False, silent=False, cache=True)
    admin = User(request_body.get('username'), request_body.get('email'))

    db.session.add(admin)
    db.session.commit()
    
    return '{"status":"SUCCESS"}' 
