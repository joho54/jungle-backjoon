#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7569                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7569                           #+#        #+#      #+#     #
#    Solved: 2025/03/29 19:08:21 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
익은 토마토만 루트가 될 수 있음.
익었는데 방문된 토마토는 어떻게 표현? 3?
-1: 토마토 없음(탐색 불가)
0: 익지 않은 토마토(탐색 가능, 모든 익지 않은 토마토는 방문하지 않은 토마토다.)
1: 익은 토마토(탐색은 가능, 모든 익은 토마토는 방문하지 않은 토마토가 아니다. )
2: 익은 방문한 토마토(탐색 가능)

3. 수도 코드
4. 코드 구현
"""
# 동, 서, 남, 북, 상, 하
dxs = [0, 0, 1, -1, 0, 0]
dys = [1, -1, 0, 0, 0, 0]
dzs = [0, 0, 0, 0, 1, -1]

EMPTY = -1
UNRIPE = 0
RIPEN_NOT_VISITED = 1
RIPEN_VISITED = 2

def in_range(x, y, z):
    return x >= 0 and x < h and y >= 0 and y < n and z >= 0 and z < m

import sys
from collections import deque

def bfs(roots: list): # only ripen tomato!
    global day
    que = deque(roots)
    # print(f'root: {root}')
    
    while que:
        is_over = True
        for _ in range(len(que)):
            x, y, z = que.pop()
            # p1: tomato[0][0][1]
            # p2: tomato[0][1][0]
            tomato[x][y][z] = RIPEN_VISITED
            # print(f'discovering {x, y, z}')
            for dx, dy, dz in zip(dxs, dys, dzs):
                nx, ny, nz = x + dx, y + dy, z + dz
                if in_range(nx, ny, nz):
                    if tomato[nx][ny][nz] == UNRIPE:
                        # print(f'tomato {nx, ny, nz} not ripped')
                        tomato[nx][ny][nz] = RIPEN_VISITED
                        que.appendleft((nx, ny, nz))
                        is_over = False
                    elif tomato[nx][ny][nz] == RIPEN_NOT_VISITED:
                        tomato[nx][ny][nz] = RIPEN_VISITED
                        que.appendleft((nx, ny, nz))
                        is_over = False
        # print(f'result on {cnt} ==========')
        if not is_over:
            day += 1
            # print(f'day update--------day {day}')
            # print_tomato(tomato)
        else:
            # print(f'day over on --- day {day}')
            return

def print_tomato(tomato):
    for i, level in enumerate(tomato):
        print(f'level {i}')
        for row in level:
            print(row)

if __name__ == "__main__":
    input = sys.stdin.readline
    m, n, h = tuple(map(int, input().split()))
    tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    # print_tomato(tomato)
    day = 0
    all_ripen = True
    while True:
        day_flag = False
        # gather roots
        roots = []
        for x in range(h):
            for y in range(n):
                for z in range(m):
                    if tomato[x][y][z] == RIPEN_NOT_VISITED:
                        roots.append((x, y, z))
                    if tomato[x][y][z] == UNRIPE:
                        all_ripen = False
        # roots = [아무튼 하나만 1이어야 함]
        if all_ripen: 
            print(0)
            sys.exit(0)
        else:
            bfs(roots)
            for x in range(h):
                for y in range(n):
                    for z in range(m):
                        if tomato[x][y][z] == UNRIPE:
                            print(-1)
                            sys.exit(0)
            # print(f'day {day}')
            # print_tomato(tomato)
            if not day_flag: 
                break


    # print('result')
    # print_tomato(tomato)
    print(day)