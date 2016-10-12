from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_filename):
    app = Flask(__name__)
    # app.config.from_pyfile(config_filename)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/users_app.db'

    from controllers import resource
    from models import User
    app.register_blueprint(resource)
    db.init_app(app)

    return app