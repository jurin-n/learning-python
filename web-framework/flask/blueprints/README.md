### 概要
* [Modular Applications with Blueprints](http://flask.pocoo.org/docs/0.11/blueprints/) 試しました。

#### virtualenv有効化
* virtualenv -p /usr/bin/python venv27
* . ~/development/virtualenv/venv27/bin/activate

#### サンプルアプリ(sample-app)起動
* pip install --editable .
* export FLASK_APP=sample-app
* flask run

#### 動作
* http://localhost:5000/sample will return index.html!!!
* http://localhost:5000/sample/admin will return admin!!!
* http://localhost:5000/sample/user will return user.html !!!!!