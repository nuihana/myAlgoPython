import sys

earth, sun, moon = map(int, sys.stdin.readline().split())

if earth == 15:
    earth = 0
if sun == 28:
    sun = 0
if moon == 19:
    moon = 0

inputYear = earth if earth != 0 else 15

while inputYear % 15 != earth or inputYear % 28 != sun or inputYear % 19 != moon:
    inputYear += 15

print(inputYear)