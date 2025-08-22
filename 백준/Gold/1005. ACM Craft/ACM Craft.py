import sys
from collections import defaultdict, deque

def solve(times: list, graph: defaultdict, w: int):
    ordered, sources = topo_sort(graph=graph)
    distances = {v:0 for v in graph}
    for source in sources: # DEBUG: 처음부터 내적이 0인 노드를 전부 거리 초기화해주지 않으면 경우에 따라 오답이 될 수 있음. ordered의 첫 요소만 초기화 할 경우 모든 경로를 고려 못함
        distances[source] = times[source] 
    
    for u in ordered:
        for v in graph[u]:
            new_d = distances[u] + times[v]
            if new_d > distances[v]:
                distances[v] = new_d
    return distances[w]                

def topo_sort(graph: defaultdict):
    indegree = {v:0 for v in graph}
    queue = deque()
    
    # set indegree
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    sources = []
    # set start points
    for u in indegree:
        if indegree[u] == 0:
            queue.append(u)
            sources.append(u)
    
    # start loop
    ordered = []
    while queue:
        # pop
        u = queue.pop()
        ordered.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return ordered, sources

if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n, k = tuple(map(int, input().split()))
        times = tuple(map(int, input().split()))
        times = {i+1:times[i] for i in range(len(times))}
        
        arr = [
            tuple(map(int, input().split()))
            for _ in range(k)
        ]
        graph = defaultdict(list)
        for u in range(1, n+1):
            graph[u] = []
        
        for u, v in arr:
            graph[u].append(v)
            
        w = int(input().strip())
        
        print(solve(times, graph, w))
