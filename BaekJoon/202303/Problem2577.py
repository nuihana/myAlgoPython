import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

result = a * b * c
usedCnt = [0 for _ in range(10)]

while result > 0:
    usedCnt[result % 10] += 1
    result //= 10

for i in range(10):
    print(usedCnt[i])
