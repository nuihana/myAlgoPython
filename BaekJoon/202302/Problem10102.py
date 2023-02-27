import sys

voteCnt = int(sys.stdin.readline().strip())

vote = sys.stdin.readline().strip()
a = 0
b = 0

for i in range(voteCnt):
    if (vote[i] == 'A'):
        a += 1
    else:
        b += 1

if (a > b):
    print('A')
elif (b > a):
    print('B')
else:
    print('Tie')
