import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    res = sys.stdin.readline().strip()
    cpr = res.lower()
    for i in range(1, n):
        tmp = sys.stdin.readline().strip()
        if tmp.lower() < cpr:
            res = tmp
            cpr = tmp.lower()

    print(res)