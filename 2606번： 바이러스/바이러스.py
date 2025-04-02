#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2606                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2606                           #+#        #+#      #+#     #
#    Solved: 2025/03/28 17:47:28 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""


# def bfs(root: int):
#     que = deque()
#     que.appendleft(root)
#     is_visited = [False for _ in range(n+1)]
#     cnt = 0
#     while que:
#         v = que.popleft()
#         for u in E[v]:
#             if not is_visited[u]:
#                 is_visited[u] = True
#                 que.appendleft(u)
#                 cnt += 1
#     return  cnt


def find_root(x):
    """x의 루트를 찾아줌."""
    if parent[x] != x:
        x = find_root(parent[x])
    return x

def union(x, y):
    x = find_root(x)
    y = find_root(y)
    if x != y:
        if y == 1: x, y = y, x
        parent[y] = x
        for i in range(len(parent)):
            if parent[i] == y:
                parent[i] = x
    
if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())
    network = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    # 처음에는 다 자기가 부모
    parent = [i for i in range(n+1)]
    for net in network:
        union(net[0], net[1])
    # print(parent)
    cnt = 0
    for p in parent:
        if p == 1:
            cnt += 1
    print(cnt-1 if cnt-1 >= 0 else 0)

    # result = bfs(1)-1 
    # result = result if result >= 0 else  0
    # print(result)
