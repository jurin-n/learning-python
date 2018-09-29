# -*- coding: utf-8 -*-
import requests

try:
    res = requests.get('https://dev1.test.local:1443/index.html')
    print(type(res.text))  # Python2.7だとunicode
    print(type(res.content))  # Python2.7だとstr
except Exception as err:
    print('Exception!' + err)


