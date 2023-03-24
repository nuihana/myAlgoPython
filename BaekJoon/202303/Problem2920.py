import sys

valArr = list(map(int, sys.stdin.readline().split()))

bfVal = 0
interval = 0
flag = True
for i in range(len(valArr)):
    if i > 0:
        if i == 1:
            interval = valArr[i] - bfVal
        else:
            if valArr[i] - bfVal != interval:
                flag = False
                break
    bfVal = valArr[i]

if flag:
    if interval > 0:
        print('ascending')
    elif interval < 0:
        print('descending')
    else:
        print('mixed')
else:
    print('mixed')