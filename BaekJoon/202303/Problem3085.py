import sys

def getMaximumLong(arr, leng):
    result = 0

    for i in range(leng):
        beforeStr = ''
        continuous = 1
        for j in range(leng):
            tmp = arr[i][j]
            if tmp == beforeStr:
                continuous += 1
            else:
                beforeStr = tmp
                continuous = 1
            result = max(result, continuous)

    for i in range(leng):
        beforeStr = ''
        continuous = 1
        for j in range(leng):
            tmp = arr[j][i]
            if tmp == beforeStr:
                continuous += 1
            else:
                beforeStr = tmp
                continuous = 1
            result = max(result, continuous)

    return result

def swapPosition(arr, fromX, fromY, toX, toY):
    tmp = arr[fromX][fromY]
    arr[fromX][fromY] = arr[toX][toY]
    arr[toX][toY] = tmp


size = int(sys.stdin.readline())
field = [['' for j in range(size)] for i in range(size)]

for i in range(size):
    str = sys.stdin.readline().strip()
    for j in range(len(str)):
        field[i][j] = str[j:j+1]

maximumCandy = 0
for i in range(size):
    for j in range(size):
        if j < size - 1:
            swapPosition(field, i, j, i, j + 1)
            maximumCandy = max(maximumCandy, getMaximumLong(field, size))
            swapPosition(field, i, j, i, j + 1)
        if i < size - 1:
            swapPosition(field, i, j, i + 1, j)
            maximumCandy = max(maximumCandy, getMaximumLong(field, size))
            swapPosition(field, i, j, i + 1, j)

print(maximumCandy)
