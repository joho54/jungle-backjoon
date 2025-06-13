"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

import sys
from collections import deque

dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

def bfs(grid: list, x: int, y: int, visited: list):
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.pop() 
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if (0 <= nx < n) and (0 <= ny < m) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))



def solve(grid: list, n: int, m: int):
    visited = [[False for _ in range(m)]for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(grid, i, j, visited)
                cnt += 1
    print(cnt)

if __name__ == '__main__':	
    input = sys.stdin.readline
    # 일단 입력
    t = int(input().strip())
    for _ in range(t):
        m, n, k = tuple(map(int, input().split()))
        grid = [[0 for _ in range(m)] for _ in range(n)]
        for _ in range(k):
            r, c = tuple(map(int, input().split()))
            grid[c][r] = 1
        solve(grid, n, m)

