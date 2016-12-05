# -*- coding: utf-8 -*-
import requests
import json

res = requests.get('https://api.github.com/users/jurin-n')
print(type(res.text))  # Python2.7だとunicode
print(type(res.content))  # Python2.7だとstr
print(json.dumps(res.json(), ensure_ascii=False)) #ダンプ結果マルチバイト文字もコードじゃ無くなる
