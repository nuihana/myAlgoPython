import sys

n = int(sys.stdin.readline())

i = 1
tmp = 0
while True:
    tmp += i
    if n - tmp <= i:
        break
    i += 1

print(i)
