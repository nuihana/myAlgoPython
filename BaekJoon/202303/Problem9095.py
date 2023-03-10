import sys


def getcase(val):
    result = 0

    result += 1  # 모든 숫자가 1의 합으로 한번 표현 가능
    for i in range(0, val, 2):
        for j in range(0, val, 3):
            if i + j <= val and (i > 0 or j > 0):
                result += multiplecombination(val - i - j, i // 2, j // 3)

    if val % 2 == 0:
        result += 1
    if val % 3 == 0:
        result += 1

    return result


def multiplecombination(one, two, thr):
    result = 1
    total = one + two + thr
    if one > 0 and two > 0 and thr > 0:
        result *= combination(total, one)
        total -= one
        result *= combination(total, two)
    else:
        if one > 0:
            result *= combination(total, one)
        elif two > 0:
            result *= combination(total, two)
        else:
            result *= combination(total, thr)

    return result


def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


def factorial(val):
    result = 1
    for i in range(1, val + 1):
        result *= i
    return result


testCnt = int(sys.stdin.readline())

for _ in range(testCnt):
    num = int(sys.stdin.readline())
    print(getcase(num))
