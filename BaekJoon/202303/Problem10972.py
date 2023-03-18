import sys

size = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

ank = -1
bfVal = 0
for i in range(size - 1, -1, -1):
    if arr[i] < bfVal:
        ank = i
        break
    bfVal = arr[i]

used = [False for _ in range(size)]
for i in range(ank):
    used[arr[i] - 1] = True

if ank == -1:
    print('-1')
else:
    tmp = 0
    for i in range(size - 1, -1, -1):
        if arr[i] > arr[ank]:
            tmp = arr[i]
            used[tmp - 1] = True
            break
    arr[ank] = tmp
    for i in range(ank + 1, size):
        for j in range(size):
            if not used[j]:
                tmp = j + 1
                used[j] = True
                break
        arr[i] = tmp

    print(' '.join(map(str, arr)))
