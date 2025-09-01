"""
풀기
문제의 목표는 뭔가요? u -> v 경로를 표현하는 그래프를 만드는 거요.
v.pi라는 속성으로, u로 가기 위한 최단 경로 시 필요한 부모 행렬을 관리하면 되겠네요. relax 함수를 그대로 구현한 후, 다익스트라를 각 노드에 대해서 
수행하면 될 거 같습니다. v.distance도 필요한 속성입니다.

"""

import sys, heapq
from collections import defaultdict

def single_source(graph: defaultdict, distances:dict, parents: dict, src: int):
    heap = []
    # 의문이 생겼어요. 다익스트라에서는 기본적으로 자신의 거리를 0으로 초기화하는데, 이걸 모든 노드에 대해서 수행하면 전부 거리가 0이 될텐데요?
    # 다익스트라를 그대로 쓰면 안 될거 같긴 하네요-> distances를 매번 새로 초기화해야 다익스트라를 제대로 쓸 수 있습니다.
    distances[src] = 0 # 출발점 0으로 초기화
    heapq.heappush(heap, (src, 0)) # 출발점과, 출발점의 거리 삽입
    
    while heap:
        u, current_distance = heapq.heappop(heap)
        
        if current_distance < distances[u]: 
            continue
        
        for neighbor, neighbor_distance in graph[u]:
            new_distance = neighbor_distance + current_distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parents[neighbor] = u
                heapq.heappush(heap, (neighbor, new_distance))

def solve(graph: defaultdict):
    ans = [
        [None for _ in range(len(graph))]
        for _ in range(len(graph))
    ]
    for key in graph:
        parents = {u:None for u in graph}
        distances = {u:float('inf') for u in graph} # distances를 매번 새로 초기화해야 다익스트라를 제대로 쓸 수 있습니다.
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