#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11725                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11725                          #+#        #+#      #+#     #
#    Solved: 2025/03/29 17:36:04 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque
def bfs(v: int):
    que = deque()
    que.appendleft(v)
    visited[v] = True
    while que:
        v = que.pop()
        for u in E[v]:
            if not visited[u]:
                visited[u] = True
                que.appendleft(u)
                parent[u] = v



if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    arr = [
        list(map(int, input().split()))
        for _ in range(n-1)
    ]
    visited = [False for _ in range(n+1)]
    E = {
        i: [] for i in range(n+1)
    }
    for v, u in arr:
        E[v].append(u)
        E[u].append(v)
    parent = [i for i in range(n+1)]
    bfs(1)
    for p in parent[2:]:
        print(p)