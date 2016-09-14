import json

json_object = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(json_object)
