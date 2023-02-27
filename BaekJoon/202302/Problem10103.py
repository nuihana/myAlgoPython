import sys

playCnt = int(sys.stdin.readline().strip())

scoreA = 100
scoreB = 100

for i in range(playCnt):
    scores = list(map(int, sys.stdin.readline().split()))
    if scores[0] > scores[1]:
        scoreB -= scores[0]
    elif scores[1] > scores[0]:
        scoreA -= scores[1]

print(scoreA)
print(scoreB)
