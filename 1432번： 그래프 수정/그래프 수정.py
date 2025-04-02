#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1432                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1432                           #+#        #+#      #+#     #
#    Solved: 2025/04/02 10:45:06 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
일단 위상정렬해서 차례로 매긴 번호를 원래 번호 순서대로 출력하면 됨.
3. 수도 코드
4. 코드 구현
"""

import sys, heapq
from collections import defaultdict


# 위상 정렬 알고리즘
def topological_sort(n: int, graph):
    # 내적 초기화
    # out_degree = [0, 0, 0, 0]
    out_degree = [0 for _ in range(n)]
    graph_reverse = defaultdict(list)
    for u in range(n):
        for v in graph[u]:
            out_degree[u] += 1
            graph_reverse[v].append(u)
    # out_degree = [2, 0, 0, 1]
    # 내적이 0인 버텍스값들 먼저 큐에 삽입
    # que = [0]
    que = [-u for u in range(n) if out_degree[u] == 0]
    heapq.heapify(que)
    cnt = n
    result = [0 for _ in range(n)]
    while que:
        for _ in range(len(que)):
            # u = 0
            u = -heapq.heappop(que)
            result[u] = cnt
            cnt -= 1
            for v in graph_reverse[u]:
                out_degree[v] -= 1
                if out_degree[v] == 0:
                    heapq.heappush(que, -v) 
    if not que and sum(out_degree) > 0:
        print(-1)
        return
    else:
        for r in result:
            print(r, end=' ')


if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    arr = [
        tuple(map(int, list(input().strip())))
        for _ in range(n)
    ]   
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                graph[i].append(j)
    topological_sort(n, graph)
    # print(graph)


