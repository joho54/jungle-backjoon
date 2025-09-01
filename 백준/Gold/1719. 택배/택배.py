"""
풀기
문제의 목표는 뭔가요? 각 u -> v의 최단 경로 상 부모 경로를 표현하는 그래프를 만들기
v.parent라는 속성으로, u로 가기 위한 최단 경로 상 필요한 부모 행렬을 관리하면 되겠네요. relax 함수를 그대로 구현한 후, 다익스트라를 각 노드에 대해서 
수행하면 될 거 같습니다. 각 노드는 v.parent, v.distance를 속성으로 가집니다.
"""

import sys, heapq
from collections import defaultdict

def single_source(graph: defaultdict, distances:dict, parents: dict, src: int):
    heap = []
    # Q. 다익스트라에서는 기본적으로 출발점의 거리를 0으로 초기화하는데, 이걸 모든 노드에 대해서 수행하면 전부 거리가 0이 될텐데요?
    # A. distances를 매번 새로 초기화해야 다익스트라를 제대로 쓸 수 있습니다. parents도 마찬가지입니다.
    distances[src] = 0 # 출발점 0으로 초기화
    # NOTE: 삽입할 때 최소힙을 고려하여 (거리, 노드 번호) 순으로 넣어야 함.
    heapq.heappush(heap, (0, src)) # 출발점과, 출발점의 거리 삽입
    
    while heap:
        current_distance, u = heapq.heappop(heap)
        
        if current_distance < distances[u]: 
            continue
        
        for neighbor, neighbor_distance in graph[u]:
            new_distance = neighbor_distance + current_distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parents[neighbor] = u
                heapq.heappush(heap, (new_distance, neighbor))

def solve(graph: defaultdict):
    ans = [
        [None for _ in range(len(graph))]
        for _ in range(len(graph))
    ]
    for key in graph:
        distances = {u:float('inf') for u in graph} # distances를 매번 새로 초기화해야 다익스트라를 제대로 쓸 수 있습니다.
        parents = {u:None for u in graph} # parent도 마찬가지로 매번 초기화를 해줘야 각 출발지에 대해 나머지 노드에 대한 최단 경로를 구할 수 있습니다.
        single_source(graph, distances, parents, key)
        for p in parents: 
            ans[p-1][key-1] = parents[p] if parents[p] is not None else '-'
    
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(ans[i][j], end=' ')
        print()

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    graph = defaultdict(list)
    arr = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]   
    for u, v, w in arr:
        graph[u].append((v, w))
        graph[v].append((u, w))        
    solve(graph)