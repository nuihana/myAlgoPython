import sys

heightList = [0] * 9

for i in range(9):
    heightList[i] = int(sys.stdin.readline())

answer = [-1] * 7

def recursearch(depth, sum, idx):
    if depth == 7:
        if sum == 100:
            answer.sort()
            for i in range(7):
                print(answer[i])
            sys.exit()
        else:
            return

    for i in range(idx, 9):
        sum += heightList[i]
        answer[depth] = heightList[i]
        recursearch(depth + 1, sum, i + 1)
        sum -= heightList[i]


recursearch(0, 0, 0)
