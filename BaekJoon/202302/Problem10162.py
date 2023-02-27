import sys

num = int(sys.stdin.readline().strip())

a = num // 300
b = num % 300 // 60
c = num % 60 // 10

if num % 10 != 0:
    print(-1)
else:
    print(f"{a} {b} {c}")
