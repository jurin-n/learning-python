# 概要
http://flask.pocoo.org/docs/0.11/tutorial/ 試しました。

#### virtualenv環境作成
mkdir ~/development/virtualenv/
mkdir ~/development/virtualenv/
virtualenv -p /usr/bin/python venv27

#### virtualenv有効化
. ~/development/virtualenv/venv27/bin/activate

#### virtualenv無効化
deactivate

#### サンプルアプリ(flaskr)起動
pip install --editable .<br/>
export FLASK_APP=flaskr<br/>
flask initdb<br/>
flask run<br/>