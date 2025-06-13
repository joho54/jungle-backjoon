
# 3
# 1 2 1
# 2 3 2
# 3
# 2 1 2
# 1 1 3
# 2 1 2

"""
1. 문제 읽기
N개의 정점으로 이루어진 트리(무방향 사이클이 없는 연결 그래프)가 있다. 정점은 1번부터 N번까지 번호가 매겨져 있고, 간선은 1번부터 N-1번까지 번호가 매겨져 있다.

아래의 두 쿼리를 수행하는 프로그램을 작성하시오.

1 i c: i번 간선의 비용을 c로 바꾼다.
2 u v: u에서 v로 가는 단순 경로에 존재하는 비용 중에서 가장 큰 것을 출력한다.

2. 문제 풀기
single source longest path를 구하는 문제.

3. 수도 코드

4. 코드 구현
"""

import sys, heapq
from collections import defaultdict

def update_edges(edges: list, graph: defaultdict):
    print("updating edge")
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))
    print("graph updated\n", graph)

def get_max_dist(single_source: int, dest: int, graph: defaultdict):
    visited = [False for _ in range(len(graph)+1)]
    distances =  [0 for _ in range(len(graph)+1)] # single_source로부터 각 노드까지의 거리. 최초 -1, 더 큰 값으로 업데이트
    distances[single_source] = 0 # 자기 자신은 0
    heap = []
    visited[single_source] = True
    heapq.heappush(heap, (0, single_source)) #single source를 힙에 삽입

    while heap:
        current_w, current_dest = heapq.heappop(heap)
        # 원래는 여기서 dist보다 힙에서 꺼낸 가중치가 크면(더 멀면) 넘어가게 돼 있음. 하지만 이제는 반대로 최적화가 되나?
        if current_w < distances[current_dest] and visited[current_dest]: 
            continue

        for neighbor_w, neighbor in graph[current_dest]: # 현재 목적지에서 인근 간선을 조회.
            new_w = neighbor_w + distances[neighbor] # 목적지의 이웃을 거쳐서 현재 목적지로 가는 경우의 가중치.
            if new_w > distances[current_dest]: # 새로운 가중치가 기존 경우에서 바로 가는 것보다 멀다면
                distances[current_dest] = new_w # 기존 가중치를 업데이트.
                # 이까지 로직은 얼추 맞는데, 그런데 뭐가 문제지? 힙에 뭘 넣어야 할지 도통 모르겠다.
                visited[current_dest] = visited
                heapq.heappush(heap, (new_w, current_dest))

    return distances[dest]

def solve(graph: defaultdict, queries: list, edges: list):
    print("initial graph\n", graph)
    for id, a1, a2 in queries:
        if(id == 1):
            edges[a1-1][2] = a2
            update_edges(edges, graph)

        if(id == 2):
            print(get_max_dist(a1, a2, graph))
    


def submit(solve, input):
    n = int(input().strip())
    graph = defaultdict(list)
    edges = [[0, 0, 0]] * (n-1) # edge number, u, v, w
    for i in range(n-1):
        u, v, w = tuple(map(int, input().split()))
        edges[i] = [u, v, w]
        graph[u].append((w, v))
        graph[v].append((w, u))
    print(edges)
    m = int(input().strip())
    queries = [[0, 0, 0]] * m
    print(queries)
    for i in range(m):
        queries[i] = tuple(map(int, input().split()))
    solve(graph, queries, edges)

if __name__ == "__main__":
    input = sys.stdin.readline

    submit(solve, input)

