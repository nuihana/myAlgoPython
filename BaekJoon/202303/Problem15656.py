import sys


def getcase(string, size, depth):
    if depth == size:
        print(string)
        return

    tmp = string
    for i in range(n):
        string += str(numArr[i]) + " "
        getcase(string, size, depth + 1)
        string = tmp


n, m = map(int, sys.stdin.readline().split())
numArr = list(map(int, sys.stdin.readline().split()))
numArr.sort()

getcase("", m, 0)
