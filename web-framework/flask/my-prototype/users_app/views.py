from flask import Blueprint

resource = Blueprint('users_app', __name__)

@resource.route('/<id>')
def get_user(id):
    return 'Hello ID=' + id +' User!!!!!!!!!'
