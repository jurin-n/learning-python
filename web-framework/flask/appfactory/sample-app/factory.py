from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.register_blueprint(resource)
    app.config.from_pyfile(config_filename)

    # from yourapplication.model import db
    # db.init_app(app)

    from view import resource
    app.register_blueprint()

    return app