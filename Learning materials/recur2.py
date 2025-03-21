def recur(n: int) -> int:
    if n > 0:
        recur(n-1)
        print(n)
        recur(n-2)

# 1. 그대로 while 문에 넣는다.

from collections import deque

def recur2(n: int) -> int:
    s = deque()
    while True:
        if n > 0: 
            # 중요한 사실: n은 이미 업데이트 된 상태다.
            # recur(n-1) # 스택에 저장을 해줄 부분과 안 해줄 부분을 구별해야 함
            s.append(n) #n을 저장하고
            n = n - 1 # 네. 이렇게 해서 n이 0보다 크면 다 1씩 줄여서 처음으로 돌아가는 겁니다. 
            continue
        if s: # 이 부분은 n이 0 보다 작을때만 출력되지 않나? 
            n = s.pop() #그러니까 n이 충분히 작아졌으면 이제 저장됐던 n을 팝해서 프린트 해주고 
            #디크레멘트해서 다시 콜 해주는 겁니다. 만약에 n이 1보다 크면 알아서 조건문에 걸릴 거고요.
            print(n)
            # recur(n-2) # 
            n = n - 2
            continue
        break
recur(4)
print("="*8)
recur2(4)