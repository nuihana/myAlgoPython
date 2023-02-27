import sys

while True:
    friendList = list(map(int, sys.stdin.readline().split()))
    if (friendList[0] == 0 and friendList[1] == 0):
        break
    print(friendList[0] + friendList[1])
