import sys

N, M = map(int, sys.stdin.readline().split())

min = min(N, M)
max = max(N, M)

print((min - 1) + (max - 1) * min)