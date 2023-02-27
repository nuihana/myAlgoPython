import sys

str = sys.stdin.readline().strip()

height = 0
bfDirection = ''

for i in range(len(str)):
    if str[i] == bfDirection:
        height += 5
    else:
        height += 10
    bfDirection = str[i]

print(height)
