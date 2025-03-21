# ring buffer!
"""
큐의 구성 요소: 
링 버퍼: 프론트, 리어
함수: 인큐, 디큐
"""

import sys

class Que():
    class FULL(Exception):
        def __init__(self, message="The que is full"):
            super().__init__(message)
    class EMPTY(Exception):
        def __init__(self, message="The que is empty"):
            super().__init__(message)
        
    _MAX_N = 2_000_000
    def __init__(self):
        self.rear = 0
        self.front = 0
        self.ring_buffer = [0] * self._MAX_N
        self.size = 0

    def is_full(self):
        if self.size == self._MAX_N: return True
        return False
    
    def is_empty(self):
        if self.size == 0: return True
        return False
    
    def enque(self, val):
        if self.is_full(): 
            raise self.FULL
        self.ring_buffer[self.rear] = val
        self.rear += 1
        self.rear %= self._MAX_N
        self.size += 1

    def deque(self):
        if self.is_empty():
            raise self.EMPTY
        tmp = self.ring_buffer[self.front]
        self.front += 1
        self.front %= self._MAX_N
        self.size -= 1
        return tmp
    
    def pop(self):
        try:
            return self.deque()
        except self.EMPTY:
            return -1

    def call_front(self):
        if self.is_empty(): return -1
        return self.ring_buffer[self.front]
    
    def call_back(self):
        if self.is_empty(): return -1
        return self.ring_buffer[self.rear-1]
    
    def empty(self):
        if self.is_empty(): return 1
        return 0

def print_q():
    global Q
    print(f'-----size: {Q.size}-------')
    for idx in range(len(Q.ring_buffer)-1, -1, -1):
        print(Q.ring_buffer[idx], end="")
        if idx == Q.rear:
            print('<----rear', end='')
        if idx == Q.front:
            print('<----front', end='')
        print()
    print('------------')


Q = Que()
n = int(sys.stdin.readline().strip())
for _ in range(n):
    command = sys.stdin.readline().split()
    arg = int(command[1]) if len(command) == 2 else None
    command = command[0]
    
    if command == 'push':
        Q.enque(arg)
    elif command == 'pop':
        print(Q.pop())
    elif command == 'size':
        print(Q.size)
    elif command == 'front':
        print(Q.call_front())
    elif command == 'back':
        print(Q.call_back())
    elif command == 'empty':
        print(Q.empty())
    # print_q()