import json
import os

from flask import Flask, request

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/echo/<thing>")
def echo(thing):
    return thing

@app.route("/json", methods=['POST'])
def post_json():
    request_body = request.get_json(force=False, silent=False, cache=True)
    return json.dumps(request_body)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
