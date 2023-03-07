import sys

inputCnt = int(sys.stdin.readline())

for _ in range(inputCnt):
    M, N, x, y = map(int, sys.stdin.readline().split())
    k = x
    if M == x:
        x = 0
    if N == y:
        y = 0
    while k % M != x or k % N != y:
        if k > M * N:
            k = -1
            break
        k += M
    print(k)
