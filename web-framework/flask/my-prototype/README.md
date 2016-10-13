## 概要
これまで読んだドキュメントを元にプロトタイプ作成しています。

## 考慮すること
* db,controller,model,logicをレイヤー化する。
* サービス別にフォルダを分ける。必要なモデルもここにまとめる。
* dbとFlask関連は共通にする。

## サンプルアプリ(sample-app)起動
* pip install --editable .
* export FLASK_APP=users_app
* flask run

## Unit Test(pytest)関連
### pytestインストール
pip install pytest
### 実行
pytest --junitxml=./test-result.xml

### 参考
http://doc.pytest.org/en/latest/usage.html
 