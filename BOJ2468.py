# 최대 인덱스는 칼럼 값 - 1이면 충분하다. 즉 in range(max_column_val) 이러면 된다.
# 이건 또 그래프가 들어가있네. 그래프 탐색을 자연스럽게 쓸 수 있을듯.

import sys  
from collections import deque

n = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, h):
    if in_range(x, y) and not visited[x][y] and grid[x][y] > h:
        return True
    return False

stack = deque()

def move(h):
    global visited, width, stack
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    while stack:
        x, y = stack.pop()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny, h):
                visited[nx][ny] = True
                # x, y를 nx, ny로 설정하고 함수의 처음으로 돌아갑니다.
                # nx, ny를 저장해줍니다.
                stack.append((nx, ny))



def simulate(h: int):
    global visited
    # 이거 뭐 하는 함수냐? 특정 높이에서 탐색하면서 영역 계산한 다음 리턴
    cnt = 0
    for i in range(n):
        for j in range(n):
            if can_go(i, j, h): # 갈 곳 없으면 알아서 재귀를 멈춘다니까.
                visited[i][j] = True
                cnt += 1
                # 한번 출발했을 때 영역 넓이를 계산해야함.
                stack.append((i, j))
                move(h)
    return cnt

# 지금 할 일: 재귀 형식의 DFS를 스택 형식으로 바꿔주기.

max_area = 0

for i in range(-1, 101):
    result = simulate(i)
    max_area = max(result, max_area)
    visited = [[False for _ in range(n)] for _ in range(n)]

print(max_area)

                


