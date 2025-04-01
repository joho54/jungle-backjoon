"""
1. 문제 읽기: 탑 번호는 1 based.
2. 문제 풀기
스택을 써서...당연히... 
팝을 한 다음, 순회를 하면서 나모다 큰 애를 만날때까지 인덱스 감소?
더 스택 논리를 활용할 수 있을 거 같은데.
팝을 하고
6 9 5 7 4
팝을 한 다음 걔들을 다른 스택에 차례로 저장하고, 
만약 팝 요소가 감소세를 보이면 쭉 가다가
증가세를 보이면? 비교해서 반대쪽에서 팝해서 인덱스를 정하면 되나? 


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
    
n = int(input())
ans = [0]*n
towers = tuple(map(int, input().split()))
towers_mapped  = [[]]*n
for i in range(n):
    towers_mapped[i] = (towers[i], i, 0)

# towers 자료구조를(높이, 자기 인덱스, 도달한 인덱스)로 관리하면 안 되나.
towers_pass1 = Stack(n)
towers_pass2 = Stack(n)

for tower in towers_mapped:
    towers_pass1.push(tower)


while not towers_pass1.is_empty():
    towers_pass2.push(towers_pass1.pop())
    while not towers_pass1.is_empty and towers_pass1.peek() < towers_pass2.peek(): # 감소세인 동안 팝 푸시 반복
        towers_pass2.push(towers_pass1.pop())
    # 만약 남아 있는 탑이 없다면
    if towers_pass1.is_empty(): 
        while not towers_pass2.is_empty():
            tower = towers_pass2.pop()
        break
    # 감소세 애들은 다 넣었고, 이제 꺼낼 애는 다 큼
    while not towers_pass2.is_empty() and towers_pass1.peek() > towers_pass2.peek():
        tower_from = towers_pass2.pop() # 뽑고, 인덱스는 어떻게 함?
        tower_to = towers_pass1.peek()
        ans[tower_from[1]] = tower_to[1]+1

for a in ans:
    print(a, end=' ')