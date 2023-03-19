import sys


def getAllCase(arr, num, depth):
    if num == depth:
        caseList.append(arr)
        return

    for i in range(num):
        tmp = arr.copy()
        if not used[i]:
            used[i] = True
            tmp.append(i)
            getAllCase(tmp, num, depth + 1)
            used[i] = False


def getDp(x, y):
    if dp[x][y] > 0:
        return dp[x][y]
    
    dp[x][y] = abs(numArr[x] - numArr[y])
    dp[y][x] = dp[x][y]
    
    return dp[x][y]


numCnt = int(sys.stdin.readline())
numArr = list(map(int, sys.stdin.readline().split()))

used = [False for _ in range(numCnt)]
caseList = []

getAllCase([], numCnt, 0)

dp = [[0 for _ in range(numCnt)] for _ in range(numCnt)]

maximum = 0
for item in caseList:
    calc = 0
    for i in range(len(item) - 1):
        calc += getDp(item[i], item[i + 1])
    maximum = max(maximum, calc)

print(maximum)