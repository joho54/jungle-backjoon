#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2252                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2252                           #+#        #+#      #+#     #
#    Solved: 2025/03/30 22:36:59 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


import sys
from collections import deque, defaultdict

def topo_sort(V_, E):
    # in degree 계산 ㄱㄱ
    in_degree = [0] * (V_+1)
    # adj list
    adj = defaultdict(list)
    V = [i for i in range(V_+1)]
    for u, v in E:
        in_degree[v] += 1
        adj[u].append(v)
    # que 생성
    que = deque([v for v in V if in_degree[v] == 0])
    result = []
    while que:
        u = que.popleft()
        result.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                que.append(v)
    del result[0]
    return result

if __name__ == '__main__':	
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    E = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    result = topo_sort(n, E)
    for r in result:
        print(r, end=' ')