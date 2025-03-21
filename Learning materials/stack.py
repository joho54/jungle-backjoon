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
    
if __name__ == "__main__":
    s = Stack(10)
    print(s)
    s.push(1)
    s.push(5)
    s.push(6)

    print(s)
    print(s.pop())
    print(s.pop())

    print("size: ", s.size())



    print(s)
    print("peek: ", s.peek())