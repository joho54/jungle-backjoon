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


def topology_sort(arr: list, n: int):
    global reversed_graph
    graph = defaultdict(list)
    in_degree = [0 for _ in range(n+1)]
    cost = [0 for _ in range(n+1)]
    for u, v, w in arr:
        graph[u].append((v, w))
        in_degree[v] += 1
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v, w in graph[u]:
            in_degree[v] -= 1
            if cost[v] <= cost[u] + w:
                if cost[v] == cost[u]+w:
                    reversed_graph[v].append(u)
                else: 
                    reversed_graph[v] = [u]
                cost[v] = cost[u] + w
            if in_degree[v] == 0:
                queue.append(v)
    return cost

def dfs(v: int):
    global reversed_graph
    stack = deque([v])
    while stack:
        v = stack.popleft()
        for u in reversed_graph[v]:
            critical_path.add((u, v))
            stack.append(u)


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
    reversed_graph = defaultdict(list)
    cost = topology_sort(arr, n)
    critical_path = set()
    dfs(end)
    print(cost[end])
    # print('critical path reversed_graph', reversed_graph)
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

5
7
1 2 1
1 3 3
2 3 2
2 4 1
4 5 1
3 5 1
2 5 3
1 5

4
5

"""