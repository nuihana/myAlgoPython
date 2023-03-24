import sys

class Node:
    value = 0
    next = None
    def __init__(self, value_):
        self.value = value_

class Queue:
    front = None
    back = None
    size = 0
    def push(self, value):
        if self.empty() == 1:
            tmp = Node(value)
            self.front = tmp
            self.back = tmp
        else:
            tmp = Node(value)
            self.back.next = tmp
            self.back = tmp
        size += 1
    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            tmp = self.front
            self.front = tmp.next
        size -= 1
    def size(self):
        return self.size
    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0
    def front(self):
        return self.front.value
    def back(self):
        return self.back.value

inputCnt = int(sys.stdin.readline())
que = Queue()

for _ in range(inputCnt):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        que.push(command[1])
    elif command[0] == 'pop':
        print(que.pop())
    elif command[0] == 'size':
        print(que.size())
    elif command[0] == 'empty':
        print(que.empty())
    elif command[0] == 'front':
        print(que.front())
    elif command[0] == 'back':
        print(que.back())
