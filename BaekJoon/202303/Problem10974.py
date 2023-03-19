import sys


def getResult(string, num, depth):
    if num == depth:
        resultList.append(string)
        return
    
    tmp = string
    for i in range(1, num + 1):
        if not used[i - 1]:
            used[i - 1] = True
            getResult(tmp + str(i), num, depth + 1)
            used[i - 1] = False


val = int(sys.stdin.readline())
used = [False for _ in range(val)]
resultList = []

getResult('', val, 0)

for item in resultList:
    print(' '.join(item))
