import sys

roopCnt = int(sys.stdin.readline())

for i in range(roopCnt):
    noAd, doAd, cost = map(int, sys.stdin.readline().split())
    doBenefit = doAd - cost
    if (doBenefit > noAd):
        print('advertise')
    elif (doBenefit == noAd):
        print('does not matter')
    else:
        print('do not advertise')
