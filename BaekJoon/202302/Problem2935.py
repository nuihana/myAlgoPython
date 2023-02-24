import sys

a = sys.stdin.readline().strip()
oper = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

if oper == '*':
    print(b + a.lstrip("1"))
elif oper == '+':
    if (len(a) > len(b)):
        print(a[:len(a) - len(b)] + b)
    elif (len(a) == len(b)):
        print(a.replace("1", "2"))
    else:
        print(b[:len(b) - len(a)] + a)
