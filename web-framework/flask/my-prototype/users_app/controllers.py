from flask import Blueprint, request
from flask import Response
from flask.json import dumps
import models

resource = Blueprint('users_app', __name__)

@resource.route('/<id>', methods=['GET'])
def get_user(id):
    user = models.get_user(id)
    return Response(dumps(user.user_dict()), status=200, mimetype='application/json')

@resource.route('/', methods=['POST'])
def post_user():
    request_body = request.get_json(force=False, silent=False, cache=True)
    
    models.add_user(request_body.get('username'), request_body.get('email'))

    return '{"status":"SUCCESS"}' 
