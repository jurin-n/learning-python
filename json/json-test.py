import json

json_object = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(json_object)

class Car():
    def __init__(self,name):
        self.name = name

car_object = Car("BMW")

json.dumps(car_object.to_JSON())
