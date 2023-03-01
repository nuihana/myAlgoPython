import sys

primeArr = [True] * 1000001

for i in range(2, 1001):
    for j in range(i + i, 1000001, i):
        primeArr[j] = False

while True:
    num = int(sys.stdin.readline().strip())

    if num == 0:
        break

    for i in range(3, len(primeArr)):
        if primeArr[i] and primeArr[num - i]:
            print(f"{num} = {i} + {num - i}")
            break
