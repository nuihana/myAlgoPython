import sys

roopCnt = int(sys.stdin.readline())
list = []

for i in range(roopCnt):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b and b == c:
        list.append(10000 + a * 1000)
    elif a == b:
        list.append(1000 + a * 100)
    elif b == c:
        list.append(1000 + b * 100)
    elif a == c:
        list.append(1000 + c * 100)
    else:
        list.append(max(a, b, c) * 100)

print(max(list))
