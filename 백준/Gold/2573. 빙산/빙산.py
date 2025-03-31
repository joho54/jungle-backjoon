#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2573                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2573                           #+#        #+#      #+#     #
#    Solved: 2025/03/29 14:04:01 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
1. 문제 읽기
2. 문제 풀기
일단 빙산 녹이기 먼저 해야 함.
이 작업을 완전 탐색 말고 방법 없지? ㅇㅇ 그리고 300 이하라서 최대 30000 칸에 대해서만 보면 됨
녹이기 연산은 거기서 더 줄어들고.
그리고 탐색 연산으로 몇 덩어리인지 판단
이걸 시뮬레이션 함수로 반복
3. 수도 코드
4. 코드 구현
"""

import sys


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def a_year_later(): # 2 * n^m
    for i in range(n):
        for j in range(m):
            if icebergs[i][j] > 0:
                get_melt_val(i, j) # n^m * 4
    for i in range(n): # n^m
        for j in range(m):
            icebergs[i][j] -= tmp_map[i][j] if icebergs[i][j] >= tmp_map[i][j] else icebergs[i][j]

def get_melt_val(x: int, y: int): # 4
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    tmp = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and icebergs[nx][ny] == 0:
            tmp += 1
    tmp_map[x][y] = tmp

from collections import deque

def bfs(x, y):
    que = deque()
    que.appendleft((x, y))
    
    visited[x][y] = True
    while que:
        x, y = que.popleft()
        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            
            if in_range(nx, ny) and icebergs[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                que.appendleft((nx, ny))    


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))  # n, m 차이에 주의!!!
    icebergs = [list(map(int, input().split())) for _ in range(n)]
    year = 0
    while True:
        year += 1
        tmp_map = [[0 for _ in range(m)] for _ in range(n)]
        a_year_later()
        # 시작지점은 완탐으로 구해야할듯?
        visited = [[False if icebergs[i][j] > 0 else True for j in range(m)] for i in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    cnt += 1
                    bfs(i, j)
                    if cnt >= 2:
                        print(year)
                        sys.exit(0)
        if cnt == 0:
            print(0)
            sys.exit(0)
