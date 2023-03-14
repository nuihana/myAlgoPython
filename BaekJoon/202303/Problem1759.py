import sys


def isvalidate(str):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    vowelCnt = 0
    consonantCnt = 0
    for item in str.replace(" ", ""):
        if item in vowels:
            vowelCnt += 1
        else:
            consonantCnt += 1
    return vowelCnt >= 1 and consonantCnt >= 2


def printPossibleStr(string, depth, pivot):
    if depth == l:
        if isvalidate(string):
            print(string.replace(" ", ""))
        return
    
    tmp = string
    for i in range(pivot, c):
        printPossibleStr(tmp + chars[i] + " ", depth + 1, i + 1)


l, c = map(int, sys.stdin.readline().split())
chars = list(sys.stdin.readline().split())
chars.sort()

printPossibleStr("", 0, 0)