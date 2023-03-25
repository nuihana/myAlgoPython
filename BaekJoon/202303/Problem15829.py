import sys

strLength = int(sys.stdin.readline())
string = sys.stdin.readline()

result = 0
r = 31
mod = 1234567891

for i in range(strLength):
    tmp = ord(string[i]) - 96
    result += tmp * pow(r, i)

print(result % mod)
