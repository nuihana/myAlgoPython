import sys

class Node:
    value = 0
    next = None
    def __init__(self, value_):
        self.value = value_
        self.next = None

class Queue:
    front = None
    back = None
    size = 0
    def __init__(self):
        self.size = 0
    def push(self, value):
        if self.empty() == 1:
            tmp = Node(value)
            self.front = tmp
            self.back = tmp
        else:
            tmp = Node(value)
            self.back.next = tmp
            self.back = tmp
        self.size += 1
    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            tmp = self.front
            if tmp.next == None:
                self.front = None
                self.back = None
            else:
                self.front = tmp.next
            self.size -= 1
            return tmp.value
    def getsize(self):
        return self.size
    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0
    def getfront(self):
        if self.front == None:
            return -1
        else:
            return self.front.value
    def getback(self):
        if self.back == None:
            return -1
        else:
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
        print(que.getsize())
    elif command[0] == 'empty':
        print(que.empty())
    elif command[0] == 'front':
        print(que.getfront())
    elif command[0] == 'back':
        print(que.getback())
