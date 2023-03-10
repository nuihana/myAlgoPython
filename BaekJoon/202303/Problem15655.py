import sys


def getcase(string, size, depth, pivot):
    if depth == size:
        print(string)
        return

    tmp = string
    for i in range(pivot, n):
        if not visited[i]:
            visited[i] = True
            string += str(numArr[i]) + " "
            getcase(string, size, depth + 1, i)
            visited[i] = False
            string = tmp
        if depth == 0:
            visited[i] = True


n, m = map(int, sys.stdin.readline().split())
numArr = list(map(int, sys.stdin.readline().split()))
numArr.sort()

visited = [False for _ in range(8)]

getcase("", m, 0, 0)
