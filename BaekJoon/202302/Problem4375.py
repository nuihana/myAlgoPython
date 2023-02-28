import sys

while True:
    input = sys.stdin.readline().strip()
    if (input is None or input == ''):
        break
    num = int(input)
    div = 1
    oneCnt = 1
    while div % num != 0:
        if div > num:
            div %= num
        div = div * 10 + 1
        oneCnt += 1
    print(oneCnt)
