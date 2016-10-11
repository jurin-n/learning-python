from flask import Flask
from view import resource

app = Flask(__name__)
app.register_blueprint(resource)
