import sys

totalScore = 0;
for i in range(5):
    tmp = int(sys.stdin.readline())
    totalScore += tmp if tmp > 40 else 40

print(totalScore // 5)
