#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1948                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1948                           #+#        #+#      #+#     #
#    Solved: 2025/04/02 17:12:36 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**8)

def topology_sort(arr: list, n: int):
    # in_degree
    graph = defaultdict(list)
    graph_reversed = defaultdict(list)
    in_degree = [0 for _ in range(n+1)]
    cost = [0 for _ in range(n+1)]
    for u, v, w in arr:
        graph[u].append((v, w))
        in_degree[v] += 1
        graph_reversed[v].append((u, w))
    queue = deque([u for u in range(n+1) if in_degree[u] == 0 ])
    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        for v, w in graph[u]:
            in_degree[v] -= 1
            if cost[v] < cost[u] + w:
                cost[v] = cost[u]+w
            if in_degree[v] == 0:
                queue.append(v)
    return cost, graph, graph_reversed

def back_prop(v: int, graph_reversed: defaultdict, path: list):
    global visited, critical_path
    # 역 추적값 구하기
    if v == start:
        # print(path)
        for p in path:
            critical_path.add(p)

    for u, w in graph_reversed[v]:
        if cost[u] == cost[v] - w and not visited[u]: # 현재 가중치를 뺀 값과 일치 ??
            visited[u] = True
            path.append((u, v))
            back_prop(u, graph_reversed, path)
            path.remove((u, v))
            visited[u] = False


if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())
    arr = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    start, end = tuple(map(int, input().split()))
    # print(n, m, arr, start, end)
    cost, graph, graph_reversed = topology_sort(arr, n)
    visited = [False for _ in range(n+1)]
    critical_path = set()
    back_prop(end, graph_reversed, [])
    print(cost[end])
    
    print(len(critical_path))


"""
5
7
1 2 1
1 3 3
2 3 2
2 4 1
2 5 3
3 5 1
4 5 1
1 5

4
5
"""