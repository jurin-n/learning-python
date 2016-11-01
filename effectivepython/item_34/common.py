# -*- coding: utf-8 -*-
import json

class Serializable(object):
    def __init__(self, *args):
        self.args = args
    
    def serialize(self):
        return json.dumps({'args':self.args})

class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])
