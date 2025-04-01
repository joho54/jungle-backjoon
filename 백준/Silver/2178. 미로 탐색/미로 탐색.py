#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2178                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2178                           #+#        #+#      #+#     #
#    Solved: 2025/03/28 18:05:32 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

def in_range(x: int, y: int):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x: int, y: int):
    if not in_range(x, y) or maze[x][y] == 0 or is_visited[x][y] != -1: 
        return False
    return True

def bfs(root: tuple):
    que = deque()
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    que.appendleft(root)
    rx, ry = root
    is_visited[rx][ry] = 1
    cnt = 1
    while que:
        x, y = que.pop() # 큐
        for dx, dy in zip(dxs, dys): # 사방을 본 다음
            nx, ny = x + dx, y + dy

            if can_go(nx, ny): # 갈 수 있으면 출발.
                # print(f'moving to {nx, ny}')
                is_visited[nx][ny] = is_visited[x][y]+1
                que.appendleft((nx, ny))
            # else: 
            #     print(f'can not go to {nx, ny}')
            #     if not in_range(nx, ny): 
            #         print('out of range')
            #     else:
            #         if maze[nx][ny] == 0: 
            #             print('maze no way')
            #         if is_visited[nx][ny]: print('already visited')
                
    return cnt

if __name__ == '__main__':	
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    maze = [
        tuple(map(int, tuple(input().strip())))
        for _ in range(n)
        ]
    is_visited = [[-1 for _ in range(m)] for _ in range(n)]
    mark_board = [[0 for _ in range(m)] for _ in range(n)]
    # for m_ in maze:
    #     print(m_)
    c = bfs((0,0))
    # print(c)
    # for v in is_visited:
    #     print(v)
    print(is_visited[n-1][m-1])