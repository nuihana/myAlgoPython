import sys

# 최대값 설정
MAX = 1000000

dp = [0] * (MAX + 1)
s = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    j = 1
    while i * j <= MAX:
        dp[i * j] += i
        j += 1
    s[i] = s[i - 1] + dp[i]

t = int(input())

for _ in range(t):
    a = int(sys.stdin.readline())
    sys.stdout.write(str(s[a])+"\n")
