import sys

roopCnt = int(sys.stdin.readline())

for i in range(roopCnt):
    data = list(sys.stdin.readline().split())
    value = float(data[0])
    for j in range(1, len(data)):
        opera = data[j]
        if opera == '@':
            value *= 3.00
        elif opera == '%':
            value += 5.00
        elif opera == '#':
            value -= 7.00

    print(f"{value:.2f}")

