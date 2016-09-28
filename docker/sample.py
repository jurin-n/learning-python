from flask import Flask,request
import json

app = Flask(__name__, static_folder=".",static_url_path="")

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

#app.run(port=80, debug=True)
app.run()
