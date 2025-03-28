#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1260                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1260                           #+#        #+#      #+#     #
#    Solved: 2025/03/28 16:42:43 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque, defaultdict

def bfs(root: int):
    que = deque()
    is_visited = [False for _ in range(n+1)] # 각 간선의 방문 여부
    que.appendleft(root)
    is_visited[root] = True
    while que:
        v = que.pop()
        print(v, end=' ')
        # 아직 방문하지 않았고 또, 여러개일 수 있으니 리스트로 만들어야 하나?
        for u in sorted(E[v]): # 정점 번호 작은 것 우선 탐색
            if not is_visited[u]:
                que.appendleft(u)
                is_visited[u] = True


def dfs(v: int, is_visited: list):
    # dfs 어떻게 구현하지? 간단하지 뭐
    print(v, end=' ')
    is_visited[v] = True
    for u in sorted(E[v]):
        if not is_visited[u]:
            is_visited[u] = True
            dfs(u, is_visited)


if __name__ == '__main__':	
    input = sys.stdin.readline
    n, m, v = tuple(map(int, input().split()))
    E = {
        i:[] for i in range(n + 1)
    }
    # print(E)
    for _ in range(m):
        u, v_ = tuple(map(int, input().split()))
        E[u].append(v_)
        E[v_].append(u)
    # print(E)
    is_visited = [False for _ in range(n+1)] # 각 간선의 방문 여부
    dfs(v, is_visited)
    print()
    bfs(v)
    print()