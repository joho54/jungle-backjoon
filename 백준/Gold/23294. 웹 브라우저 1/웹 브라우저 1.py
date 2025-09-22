# label: 자료구조 종합 + 구현

import sys
from collections import deque

def solve(n: int, q: int, c: int, cap: tuple, tasks: list):
    
    BQ = deque()
    FQ = deque()
    current_page = None
    using_cache = 0
    
    
    for task in tasks:
        if task[0] == 'B' and BQ:
            if current_page: 
                FQ.append(current_page)
            current_page = BQ.pop()
            
        elif task[0] == 'F' and FQ:
            if current_page: 
                BQ.append(current_page)
            current_page = FQ.pop()
            
        elif task[0] == 'A':
            for page in FQ:
                using_cache -= cap[page]
            FQ.clear()
            if current_page: # 처음 접속한게 아니라면
                BQ.append(current_page)
            current_page = int(task[1])
            using_cache += cap[current_page] # update using cache 
            
            while using_cache > c:
                using_cache -= cap[BQ.popleft()]  # 삭제는 fifo
                
        elif task[0] == 'C':
            removal_indices = []
            for i in range(0, len(BQ)-1): 
                if BQ[i+1] == BQ[i]:  # 
                    removal_indices.append(i+1) # 삭제할 인덱스를 모두 포함: 가장 최근을 남겨야 하는데 (근데 최근이든 뭐든 상관 없어 보이는데.)
                    using_cache -= cap[BQ[i+1]] # 캐시 감소
            
            BQ = deque([BQ[i] for i in range(len(BQ)) if i not in removal_indices])
            
    # 출력
    print(current_page)
    if BQ:
        while BQ:
            print(BQ.pop(), end=' ')
        print()
    else: 
        print(-1)
    if FQ:
        while FQ:
            print(FQ.pop(), end=' ')
        print()
    else:
        print(-1)
        
if __name__ == '__main__':
    input = sys.stdin.readline
    n, q, c = tuple(map(int, input().split()))
    cap = [0] + list(map(int, input().split())) # 각 페이지의 사이즈임
    tasks = [
        input().split()
        for _ in range(q)
    ]
    solve(n, q, c, cap, tasks)    
    

