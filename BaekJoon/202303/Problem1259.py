import sys


def isPalindrome(value):
    left = 0
    right = len(value) - 1
    while left < right:
        if value[left] != value[right]:
            return False
        left += 1
        right -= 1
    return True


while True:
    value = sys.stdin.readline().strip()
    if value == '0':
        break
    if isPalindrome(value):
        print('yes')
    else:
        print('no')
