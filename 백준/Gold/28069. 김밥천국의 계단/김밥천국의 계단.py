import sys
from collections import deque

def solve(n: int, memo_depth: list): 
    queue = deque()
    queue.append((1, 1)) 
    
    while queue:
        i, depth = queue.popleft() # DEBUG: queue.pop()은 DFS로 동작(LIFO). FIFO로 관리해야 함.
        
        if i > n:
            continue
        if memo_depth[i] <= depth:
            continue

        memo_depth[i] = depth
        queue.append((i+1, depth+1))
        queue.append((i+(i//2), depth+1))

if __name__ == '__main__':
    input = sys.stdin.readline
    
    n, k = tuple(map(int, input().split()))
    memo_depth = [sys.maxsize for _ in range(n+1)]
    solve(n, memo_depth)
    
    if memo_depth[n] <= k:
        print('minigimbob')
    else:
        print('water')