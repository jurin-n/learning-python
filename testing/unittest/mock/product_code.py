# -*- coding: utf-8 -*-

import requests

# This is the class we want to test
class MyGreatClass:
    def fetch_json(self, url):
        response = requests.get(url)
        return response.json()


def fetch_json(url):
    response = requests.get(url)
    return response.json()