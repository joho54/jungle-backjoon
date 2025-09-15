import sys
from collections import deque

def bfs(r, c, x, y, grid:list, visited: list):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    sheep, wolves = 0, 0
    while queue:
        x, y = queue.popleft()
        if grid[x][y] == 'k': sheep += 1
        elif grid[x][y] == 'v': wolves += 1
        
        for dx, dy in zip([0 ,0, -1, 1], [1, -1, 0, 0]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] != '#' and not visited[nx][ny]: # 범위 내에 있고, 울타리가 아니고, 방문하지 않았다면
                visited[nx][ny] = True
                queue.append((nx, ny))
    if sheep > wolves:
        wolves = 0
    else:
        sheep = 0
    return sheep, wolves

def solve(r: int, c: int, grid: list):
    visited = [[False] * c for _ in range(r)]
    total_sheep, total_wolves = 0, 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] != '#' and not visited[i][j]:
                sheep, wolves =  bfs(r, c, i, j, grid, visited)
                total_sheep += sheep
                total_wolves += wolves
    return f'{total_sheep} {total_wolves}'

if __name__ == '__main__':
    input = sys.stdin.readline
    r, c = tuple(map(int, input().split()))
    grid = [
        input().strip()
        for _ in range(r)
    ]
    
    print(solve(r, c, grid))