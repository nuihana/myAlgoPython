import sys

conditionCnt = int(sys.stdin.readline())
conditionArr = list(sys.stdin.readline().split())
used = [0] * 10

idx = 9
maxResult = []
stack = []

for i in range(len(conditionArr)):
    if conditionArr[i] == ">":
        if len(stack) == 0:
            maxResult.append(str(idx))
        else:
            stack.append(idx)
            while len(stack) != 0:
                maxResult.append(str(stack.pop()))
    elif conditionArr[i] == "<":
        stack.append(idx)
    idx -= 1
if len(stack) == 0:
    maxResult.append(str(idx))
else:
    stack.append(idx)
    while len(stack) != 0:
        maxResult.append(str(stack.pop()))

print(''.join(maxResult))

idx = 0
minResult = []

for i in range(len(conditionArr)):
    if conditionArr[i] == "<":
        if len(stack) == 0:
            minResult.append(str(idx))
        else:
            stack.append(idx)
            while len(stack) != 0:
                minResult.append(str(stack.pop()))
    elif conditionArr[i] == ">":
        stack.append(idx)
    idx += 1
if len(stack) == 0:
    minResult.append(str(idx))
else:
    stack.append(idx)
    while len(stack) != 0:
        minResult.append(str(stack.pop()))

print(''.join(minResult))
