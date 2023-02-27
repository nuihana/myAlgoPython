import sys

voteCnt = int(sys.stdin.readline().strip())

yes = 0
no = 0

for i in range(voteCnt):
    answer = int(sys.stdin.readline().strip())
    if (answer == 1):
        yes += 1
    else:
        no += 1

if (yes > no):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
