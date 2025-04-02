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
    # 내적 초기화
    # e. in_degree = [0, 0, 0, 0, 0, ]
    in_degree = [0]*(V+1)
    # 인접 리스트 초기화
    adj = defaultdict(list)
    # v 초기화
    V_ = [i for i in range(V+1)]
    # 가중치
    weights = defaultdict(int)
    
    # p1. 5, 1, 2
    # p2. 5, 2, 2
    # p3. ...
    for v, u, w in E:
        adj[u].append(v)
        in_degree[v] += 1
        weights[(u,v)] = w
    result = []
    # 내적이 0인 버텍스 초기화
    
    initials = [v for v in V_ if in_degree[v] == 0]
    # initials = [1, 2, 3, 4]
    for i in initials:
        p[i-1][i-1] = 1 # 자기자신을 만들 때 하나씩 필요

    que = deque(initials)
    que.popleft() # 0 제거
    # que = deque([1, 2, 3, 4])
    while que:
        # p1. u = 1
        u = que.popleft()
        # p1. result = [1]
        result.append(u)
        # 내적을 제거하고 위상정렬. v를 만드는데 u가 가중치만큼 필요할 것.
        # pick: u = 6
        for v in adj[u]:
            # v 내적 제거
            # v 부품 만들때 필요한 정보 업데이트. u번째 부품이 몇 개 필요한가?
            # 기존 u의 내적값...아 여기서 모든 부품에 대한 이터레이션 필요
            # p1. i = 0 
            # p2. i = 1
            # n = 7
            # 6번 부품이 7번부품 만들 때 몇개 필요한지 반영이 안 됨
            # pick: 
            for i in range(n):
                # i = 0
                # p[v-1=6][0~6] += p[5][0~6]*weight
                p[v-1][i] += p[u-1][i]*weights[(u,v)]
            
            in_degree[v] -= 1
            if in_degree[v] == 0:
                que.append(v)

    for i in initials:
        if i != 0:
            print(i, p[n-1][i-1] )

def dag_shortest_path(s:int, adj: list, weights: list):
    """뭐 어떻게 하면 되지? 일단 하나의 버텍스를 기준으로? 그냥 모든 간선을 돌면서?"""
    p[s] = 1
    que = deque([s])
    while que:
        u = que.popleft()
        for v in adj[u]:
            que.append(v)



if __name__ == '__main__':	
    input = sys.stdin.readline
    # n = 7
    n = int(input().strip()) 
    # m = 8
    m = int(input().strip())
    # E = [(5, 1, 2), ...]
    # 
    E = [ 
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    # p는? i번째 부품을 만드는데 m번째 부품이 몇 개 필요한지 계산.
    """
    p = [ 
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    """
    p = [[0 for j in range(n)] for _ in range(n)]
    topological_sort(n, E)
    # for s in p:
    #     print(s)
    # for s in initials:
    #     p = [0 for _ in range(n+1)]
    #     dag_shortest_path(s, adj, weights)
    #     print(f'{s} {p[n]}')

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