from package import daily, weekly
import sys

print("#パッケージ packageのdailyとweeklyをつかいprint#")
print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)

print("#モジュールのサーチパス表示#")
for place in sys.path:
    print(place)
