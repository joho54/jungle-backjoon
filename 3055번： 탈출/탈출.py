import sys
from collections import deque

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
NO_WATER = -2
HODGE_VISITED = -3
INIT_WATER = -1

def bfs():
    global water_time
    queue = deque()
    for r, c in water_source:
        water_time[r][c] = 0
        queue.append((r, c))
    water_time[dest[0]][dest[1]] = float('inf')
    cnt = 0
    
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y = queue.popleft() 
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and water_time[nx][ny] == INIT_WATER:
                    if forest[nx][ny] == 'X':
                        water_time[nx][ny] = NO_WATER # NO_WATER라서 비버도 절대 못 감
                    elif forest[nx][ny] == 'D': # 목적지는
                        water_time[nx][ny] = float('inf')
                    else: 
                        water_time[nx][ny] = cnt
                        queue.append((nx, ny))

def in_range(x, y):
    return x >= 0 and x < r and y >= 0 and y < c
        
def bfs_hodge(s: tuple):
    queue = deque([s])
    water_time[s[0]][s[1]] = HODGE_VISITED
    cnt  = 0 
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) \
                and (water_time[nx][ny] > cnt\
                or water_time[nx][ny] == INIT_WATER)\
                    and not forest[nx][ny] == 'X'\
                    and water_time[nx][ny] != HODGE_VISITED: # 물이 도달하는 시간이 느리거나 (돌은 NO_WATER라서 배재됨. -1이라서 안 오거나)
                    if (nx, ny) == dest:
                        print(cnt)
                        return
                    queue.append((nx, ny))
                    water_time[nx][ny] = HODGE_VISITED
        # for wt in water_time:
        #     print(wt)
    print('KAKTUS')
    return

if __name__ == '__main__':	
    input = sys.stdin.readline
    r, c = tuple(map(int, input().split()))
    forest = [
        list(input().strip())
        for _ in range(r)
    ]

    water_time = [[INIT_WATER for _ in range(c)]for _ in range(r)]
    water_source = []
    for i in range(r):
        for j in range(c):
            if forest[i][j] == '*':
                water_source.append((i, j))
            if forest[i][j] == 'D':
                dest = (i, j)
            if forest[i][j] == 'S':
                start = (i, j)
    bfs()
    # for wt in water_time:
    #     print(wt)
    bfs_hodge(start)

# 고슴도치가 움직일 수 있는 방법. 고슴도치 데이가 있고, 
# 그 값보다 이동하려는 water_time 값이 커야 이동 가능.
# -1은 그럼 나쁜 비교가 되는데? 무한으로 바꿔서 항상 이동 가능하게 해야함
# [-1, 3, 2, 1, 0, 1]
# [7, -1, 3, -1, 1, 2]
# [6, 5, 4, 3, 2, 3]