
import sys

class Stack:
    def __init__(self):
        self.MAX_N = 1000000
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
    
def is_VPS(string: str):
    for parenthesis in string:
        if parenthesis == '(':
            stack.push(1)
        elif parenthesis == ')':
            if stack.pop() == -1: 
                return False
    return stack.is_empty()


n = int(sys.stdin.readline().strip())
for _ in range(n):
    stack = Stack()
    s = sys.stdin.readline().strip()
    print('YES') if is_VPS(s) else print('NO')
