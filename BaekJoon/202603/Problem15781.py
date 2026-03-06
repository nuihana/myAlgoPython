import sys

n, m = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))

maxH = max(h)
maxA = max(a)

print(maxH + maxA)