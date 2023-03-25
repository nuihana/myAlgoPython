import sys


def getAllCase():
    if len(case) == cityCnt:
        global cost
        tmp = 0
        for i in range(cityCnt - 1):
            if costArr[case[i] - 1][case[i + 1] - 1] == 0:
                tmp = 10000000
                break
            tmp += costArr[case[i] - 1][case[i + 1] - 1]
        if costArr[case[cityCnt - 1] - 1][case[0] - 1] == 0:
            tmp = 10000000
        else:
            tmp += costArr[case[cityCnt - 1] - 1][case[0] - 1]
        cost = min(tmp, cost)
        return

    for i in range(2, cityCnt + 1):
        if i not in case:
            case.append(i)
            getAllCase()
            case.pop()


cityCnt = int(sys.stdin.readline())
costArr = [[0 for _ in range(cityCnt)] for _ in range(cityCnt)]

for i in range(cityCnt):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(cityCnt):
        costArr[i][j] = line[j]

case = [1]

cost = 10000000
getAllCase()

print(cost)
