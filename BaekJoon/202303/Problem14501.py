import sys


def getMaximumBenefit(summary, start):
    tmp = summary
    result = 0
    for i in range(start, dateCnt):
        if not reserved[i] and dateCnt - i >= consulting[i][0]:
            setReserve(i)
            result = max(result, getMaximumBenefit(tmp + consulting[i][1], i + consulting[i][0]))
            setCancel(i)
    result = max(result, summary)
    return result
        

def setReserve(idx):
    for i in range(idx, consulting[idx][0] + idx):
        reserved[i] = True


def setCancel(idx):
    for i in range(idx, consulting[idx][0] + idx):
        reserved[i] = False


dateCnt = int(sys.stdin.readline())
consulting = [[0 for _ in range(2)] for _ in range(dateCnt)]
reserved = [False for _ in range(dateCnt)]

for i in range(dateCnt):
    tmp = list(map(int, sys.stdin.readline().split()))
    consulting[i][0] = tmp[0]
    consulting[i][1] = tmp[1]

print(getMaximumBenefit(0, 0))
