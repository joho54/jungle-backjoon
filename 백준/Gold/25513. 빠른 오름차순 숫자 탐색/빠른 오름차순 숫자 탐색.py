# label: BFS. 
# 주의사항: 1, 2, 3, 4, 5, 6은 무조건 주어지고, -1은 방문 불가. visited도 각각의 BFS에서 매번 다시 갈 수 있음.

import sys
from collections import deque

def bfs(current_pos: tuple, next_val: int, visited: list, grid: list) -> tuple:
    queue = deque()
    # current_pos -> next_pos where it is next_val 
    queue.append((*current_pos, 0))
    while queue:
        r, c, cnt = queue.popleft() # DEBUG: popleft로 해야 큐로 동작함
        for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
            nx, ny = r + dx, c + dy
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and grid[nx][ny] != -1:
                visited[nx][ny] = True
                if grid[nx][ny] == next_val:
                    # print('-'*10)
                    # for row in visited:
                    #     print(row)
                    return (nx, ny), cnt+1
                queue.append((nx, ny, cnt+1))
    return (-1, -1), -1      
                
    

def solve(r, c, grid: list):
    current_pos = (r, c)
    cnt = 0
    for next_val in range(1, 7):
        visited = [[False] * 5 for _ in range(5)]
        visited[current_pos[0]][current_pos[1]] = True
        current_pos, tmp_cnt = bfs(current_pos, next_val, visited, grid)
        if tmp_cnt == -1:
            return -1
        # print(tmp_cnt)
        cnt += tmp_cnt
    return cnt
        
        

if __name__ == '__main__':
    input = sys.stdin.readline
    grid = [
        tuple(map(int, input().split()))
        for _ in range(5)
    ]
    r, c = tuple(map(int, input().split()))
    print(solve(r, c, grid))