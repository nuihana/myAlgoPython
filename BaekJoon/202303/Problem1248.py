import sys

valSize = int(sys.stdin.readline())
valLine = sys.stdin.readline()

valArr = [['-1' for _ in range(valSize)] for _ in range(valSize)]

idx = 0
for i in range(valSize):
    for j in range(i, valSize):
        valArr[i][j] = valLine[idx:idx+1]
        idx += 1

result = [0 for _ in range(valSize)]
vector = [0 for _ in range(valSize)]
for i in range(valSize):
    if valArr[i][i] == '-':
        result[i] = -1
        vector[i] = -1
    elif valArr[i][i] == '+':
        result[i] = 1
        vector[i] = 1

pivotX = 0
while pivotX < valSize:
    flag = True
    for i in range(pivotX + 1):
        condition = 0
        if valArr[i][pivotX] == '-':
            condition = -1
        elif valArr[i][pivotX] == '+':
            condition = 1
        
        partSum = 0
        for j in range(i, pivotX + 1):
            partSum += result[j]
        
        if condition == 1:
            if partSum <= 0:
                flag = False
                tmp = pivotX
                while tmp > 0:
                    if vector[tmp] > 0:
                        result[tmp] += 1
                        pivotX = tmp
                        break
                    tmp -= 1
                break
        elif condition == 0:
            if partSum > 0:
                flag = False
                tmp = pivotX
                while tmp > 0:
                    if vector[tmp] < 0:
                        result[tmp] -= 1
                        pivotX = tmp
                        break
                    tmp -= 1
                break
            elif partSum < 0:
                flag = False
                tmp = pivotX
                while tmp > 0:
                    if vector[tmp] > 0:
                        result[tmp] += 1
                        pivotX = tmp
                        break
                    tmp -= 1
                break
        elif condition == -1:
            if partSum >= 0:
                flag = False
                tmp = pivotX
                while tmp > 0:
                    if vector[tmp] < 0:
                        result[tmp] -= 1
                        pivotX = tmp
                        break
                    tmp -= 1
                break
    if flag:
        pivotX += 1

resultStr = ''
for item in result:
    resultStr += str(item) + ' '

print(resultStr)