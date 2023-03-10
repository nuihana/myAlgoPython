import sys

zero = [1, 0, 1]
one = [0, 1, 1]


def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(f"{zero[num]} {one[num]}")


testCnt = int(sys.stdin.readline())
dp = [0 for _ in range(40)]

for _ in range(testCnt):
    number = int(sys.stdin.readline())
    fibonacci(number)
