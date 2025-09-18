# label: graph

import sys
from collections import deque

ME = 'ME'
OBSTACLE = '@'
SINK = 'S'
EMPTY = '.'

def bfs(n: int, grid: list, i: int, j: int, visited: list):
    queue = deque()
    queue.append((i, j))
    
    if visited[i][j]:
        return 0
    visited[i][j] = True
    while queue:
        x, y = queue.popleft() 
        for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
            nx, ny = x + dx, y + dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and grid[nx][ny] == EMPTY: 
                queue.append((nx, ny))
                visited[nx][ny] = True  
    return 1

def solve(n: int, grid: list, debug: bool = False):
    ans = 0 
    for i in range(n):
        for j in range(n):
            if grid[i][j] == EMPTY:
                # 여러 변수 초기화
                grid[i][j] = ME
                src = []
                logic_mul = True
                visited = [[False]*n for _ in range(n)]
                
                # 잠복한 나를 중심으로 상하좌우에 이동 가능 영역 탐색
                for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                    nx, ny = i + dx, j + dy
                    if 0<=nx<n and 0<=ny<n and grid[nx][ny] == EMPTY: 
                        src.append((nx, ny))
                if debug:
                    print(src)
                # 이동 가능한 영역의 개수가 1개 이하라면 '건너서 갈 수 있는 공간'이 없음.
                if len(src) < 2: 
                    logic_mul = False
                
                # 각 출발지를 토대로 해당 영역들이 여행 가능한지 확인.
                partitions = 0
                for a_src in src:
                    partitions += bfs(n, grid, a_src[0], a_src[1], visited)
                if partitions >= 2:
                    ans += 1
                if debug:
                    if logic_mul:
                        print('GOT IT!!!')
                    print('-'*20)
                    for row in grid:
                        print(row)
                grid[i][j] = EMPTY
    return ans
                

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    grid = [
        list(input().strip())
        for _ in range(n)
    ]
    print(solve(n, grid, False))
    
'''


4
@@@@
..@.
..@.
....

4
@@@@
..@.
..@.
@...

'''