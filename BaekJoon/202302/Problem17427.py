import sys

num = int(sys.stdin.readline().strip())

result = 0
for i in range(1, num + 1):
    result += (num // i) * i

print(result)
