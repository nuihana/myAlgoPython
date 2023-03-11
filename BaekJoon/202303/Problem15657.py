import sys


def getcase(string, size, depth, pivot):
    if depth == size:
        print(string)
        return

    tmp = string
    for i in range(pivot, n):
        string += str(numArr[i]) + " "
        getcase(string, size, depth + 1, i)
        string = tmp


n, m = map(int, sys.stdin.readline().split())
numArr = list(map(int, sys.stdin.readline().split()))
numArr.sort()

getcase("", m, 0, 0)
