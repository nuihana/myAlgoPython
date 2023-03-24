import sys

numArr = list(map(int, sys.stdin.readline().split()))

summary = 0
for item in numArr:
    summary += pow(item, 2)

print(summary % 10)