import sys

testCase = int(sys.stdin.readline().strip())

for i in range(testCase):
    collegeCnt = int(sys.stdin.readline().strip())
    collegeArr = []
    maxIdx = -1
    maxConsume = -1
    for j in range(collegeCnt):
        infos = list(sys.stdin.readline().split())
        collegeArr.append(infos[0])
        if maxConsume < int(infos[1]):
            maxIdx = j
            maxConsume = int(infos[1])
    print(collegeArr[maxIdx])

