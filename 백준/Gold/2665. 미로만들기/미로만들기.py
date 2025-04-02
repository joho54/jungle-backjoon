#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2665                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2665                           #+#        #+#      #+#     #
#    Solved: 2025/03/31 21:16:37 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys, heapq
from collections import deque

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bfs_var():
    # init starting point
    maze_time[0][0] = 0
    queue = [[0, 0, 0]]

    while queue:
        _, x, y = heapq.heappop(queue)
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            # 여기서 그 최적화를 해줄 수 있다. 
            if in_range(nx, ny):
                if maze[nx][ny] == 0: w = 1
                else: w = 0
                if maze_time[x][y] + w > maze_time[nx][ny]:
                    continue
                distance = maze_time[x][y]+w
                if distance < maze_time[nx][ny]:
                    maze_time[nx][ny] = distance
                    heapq.heappush(queue, (distance, nx, ny))
    # print('-'*10)
    # for mt in maze_time:
    #     print(mt)

if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    maze = [
        tuple(map(int, list(input().strip())))
        for _ in range(n)
    ]
    # for m in maze:
    #     print(m)
    maze_time = [
        [float('inf') for _ in range(n)]
        for _ in range(n)
    ]
    bfs_var()
    print(maze_time[n-1][n-1])

"""
8
11100110
11010010
10011010
11101100
01100111
00110001
11011100
11000111
"""