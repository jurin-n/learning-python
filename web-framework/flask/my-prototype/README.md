## 概要
これまで読んだドキュメントを元にプロトタイプ作成しています。

## 考慮すること
* db,controller,model,logicをレイヤー化する。
* サービス別にフォルダを分ける。必要なモデルもここにまとめる。
* dbとFlask関連は共通にする。

#### サンプルアプリ(sample-app)起動
* pip install --editable .
* export FLASK_APP=users_app
* flask run