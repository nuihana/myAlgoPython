import sys

k, n, m = map(int, sys.stdin.readline().split())

need = k * n - m

if need >= 0:
    print(need)
else:
    print(0)
