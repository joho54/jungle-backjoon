"""
1. 문제 읽기
2. 문제 풀기
차례대로 막대기 푸시하다가 탑보다 큰게 오면 팝하고 푸시하면 되겠다.
3. 수도 코드
4. 코드 구현
"""

class Stack:
    def __init__(self, size):
        self.stack = [0] * size
        self.ptr = 0

    class Empty(Exception):
        def __init__(self, message="Stack is empty"):
            self.message= message
            super().__init__(self.message)

    class Full(Exception):
        def __init__(self, message="Stack is full"):
            self.message = message
            super().__init__(self.message)

    def is_empty(self):
        return self.ptr == 0
    
    def is_full(self):
        return self.ptr == self.size

    def __str__(self):
        return f'{self.stack[:self.ptr]}'
    
    def clear(self):
        self.ptr = 0

    def peek(self):
        if self.is_empty(): raise Stack.Empty
        return self.stack[self.ptr-1]
    
    def push(self, n):
        if self.is_full(): raise Stack.Full
        self.stack[self.ptr] = n
        self.ptr += 1

    def pop(self):
        if self.is_empty(): raise Stack.Empty
        tmp = self.stack[self.ptr-1] 
        self.ptr -= 1
        return tmp
    
    def size(self):
        return self.ptr
    
import sys

stack = Stack(100_000)
n = int(sys.stdin.readline().strip())
for _ in range(n):
    stick = int(sys.stdin.readline().strip())
    # print(f'stack empty? {stack.is_empty()}')
    while not stack.is_empty() and stack.peek() <= stick:
        stack.pop() # 뽑아버리고
    stack.push(stick) # 푸시
    # print(stack)


print(stack.size())