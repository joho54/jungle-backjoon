# 그냥 스택 만들기~

import sys

class Stack:
    def __init__(self):
        self.MAX_N = 10000
        self.stack = [0]*self.MAX_N
        self.sp = 0

    def is_full(self):
        return self.sp >= self.MAX_N
    
    def is_empty(self):
        return self.sp <= 0

    def push(self, val):
        if self.is_full(): return -1
        self.stack[self.sp] = val
        self.sp += 1
    
    def pop(self):
        if self.is_empty(): return -1
        self.sp -= 1
        return self.stack[self.sp]
    
    def size(self):
        return self.sp
    
    def empty(self):
        return 1 if self.is_empty() else 0
    
    def top(self):
        if self.is_empty(): return -1
        return self.stack[self.sp-1]

s = Stack()
n = int(sys.stdin.readline().strip())
for _ in range(n):
    command = sys.stdin.readline().split()
    arg = int(command[1]) if len(command) == 2 else None
    command = command[0]
    if command == 'push':
        s.push(arg)
    elif command == 'pop':
        print(s.pop())
    elif command == 'size':
        print(s.size())
    elif command == 'empty':
        print(s.empty())
    elif command == 'top':
        print(s.top())


