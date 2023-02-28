import sys

matchCnt = int(sys.stdin.readline().strip())

for i in range(matchCnt):
    yonsei = 0
    korea = 0
    for j in range(9):
        scores = list(map(int, sys.stdin.readline().split()))
        yonsei += scores[0]
        korea += scores[1]
    if (yonsei > korea):
        print('Yonsei')
    elif (korea > yonsei):
        print('Korea')
    else:
        print('Draw')
