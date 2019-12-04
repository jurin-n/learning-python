# -*- coding: utf-8 -*-

import datetime

jst=datetime.timezone(datetime.timedelta(hours=+9))
d=datetime.datetime.fromtimestamp(150000000)

# タイムゾーン無し
print(str(d))
print(d.isoformat())

# タイムゾーン有り(+09:00 Asia/Tokyo)
print(d.astimezone(jst))
print(d.astimezone(jst).isoformat())

