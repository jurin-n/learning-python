import re

url_scheme1 = '/users/(?P<user_id>\w+\d+-\w+\d+)'
url_scheme2 = '/users/(?P<user_id>\d+)'

pattern1 = re.compile(url_scheme1)
pattern2 = re.compile(url_scheme2)

print(pattern1.match('/users/u01-z01').groupdict())
print(pattern1.match('/users/u01-z02').groupdict())
print(pattern2.match('/users/001').groupdict())

try:
    print(pattern2.match('/users/u01').groupdict())
except:
    print("pattern2.match('/users/u01') is error.")
