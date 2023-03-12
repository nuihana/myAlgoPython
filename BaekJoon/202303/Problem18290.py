import sys


def tryall(x, y, sum_, idx):
    if idx == k:
        return sum_

    tmp = sum_
    result = -50000
    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            if visited[i][j] == 0:
                setvisited(i, j)
                result = max(result, tryall(i, j, tmp + arr[i][j], idx + 1))
                setleaved(i, j)
    return result


def setvisited(x, y):
    visited[x][y] += 1
    if x > 0:
        visited[x - 1][y] += 1
    if y > 0:
        visited[x][y - 1] += 1
    if x < n - 1:
        visited[x + 1][y] += 1
    if y < m - 1:
        visited[x][y + 1] += 1


def setleaved(x, y):
    visited[x][y] -= 1
    if x > 0:
        visited[x - 1][y] -= 1
    if y > 0:
        visited[x][y - 1] -= 1
    if x < n - 1:
        visited[x + 1][y] -= 1
    if y < m - 1:
        visited[x][y + 1] -= 1


n, m, k = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))

print(tryall(0, 0, 0, 0))
