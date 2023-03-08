import sys

num = int(sys.stdin.readline())

result = 0

size = len(str(num))
dividor = 1

for _ in range(1, size):
    dividor *= 10

while size > 0:
    result += (num - dividor + 1) * size
    num = dividor - 1
    dividor //= 10
    size -= 1

print(result)