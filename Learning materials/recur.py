from collections import deque

def recur(n):
    if n <= 0: 
        return # n이 0보다 작으면 아무 작업하지 않는다.
    
    recur(n-1) # 이 세 줄의 코드가 트리형으로 갑니다.
    print(n)
    recur(n-2) #n-2로 업데이트하고 함수의 처음으로 돌아갑니다.


# 1. 꼬리 재귀 제거
# 2. 중간 재귀 제거 및 스택 저장 과정을 추가.

def recur2(n):
    s = deque()
    s.append(n) # ?
    while True:
        if n > 0:
            s.append(n)
            n = n - 1
            continue
        if s:
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break


recur(4)
print('='*8)
recur2(4)