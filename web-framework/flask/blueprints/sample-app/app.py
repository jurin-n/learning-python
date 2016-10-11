from flask import Flask
from view import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

print app.url_map
print app.template_folder
print simple_page.root_path


if __name__ == '__main__': 
    app.run(debug=True)