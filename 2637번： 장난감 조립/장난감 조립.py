#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2637                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2637                           #+#        #+#      #+#     #
#    Solved: 2025/03/30 22:45:21 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# 아니 이거는 그거잖아. 
#  위상정렬을 하고, shortest path estimate 대신 all paths estimate로 노드를 업데이트하면
# 되지 않겠나?

import sys
from collections import deque, defaultdict
# 그래프 표현 컨벤션을 너무 섞어 쓰는 거 같다.
def topological_sort(V: int, E):
    in_degree = [0]*(V+1)
    adj = defaultdict(list)
    V_ = [i for i in range(V+1)]
    weights = defaultdict(int)
    for v, u, w in E:
        adj[u].append(v)
        in_degree[v] += 1
        weights[(u,v)] = w
    result = []
    initials = [v for v in V_ if in_degree[v] == 0]
    que = deque(initials)
    while que:
        u = que.popleft()
        result.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                que.append(v)
    return result, adj, initials, weights
    

def dag_shortest_path(s:int, adj: list, weights: list):
    """뭐 어떻게 하면 되지? 일단 하나의 버텍스를 기준으로? 그냥 모든 간선을 돌면서?"""
    p[s] = 1
    que = deque([s])
    while que:
        u = que.popleft()
        for v in adj[u]:
            p[v] += p[u]*weights[(u,v)]
            que.append(v)



if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())
    E = [ 
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    result, adj, initials, weights = topological_sort(n, E)
    for s in initials:
        p = [0 for _ in range(n+1)]
        dag_shortest_path(s, adj, weights)
        print(f'{s} {p[n]}')

"""
이슈: 시간초과

Phase1.
환경: 파이썬
로그: 
최근 변경 사항: 

Phase2.
확인: 
시도: 
p 초기화 함수 삭제,
relax 함수 삭제

분석: 의미 없음
"""