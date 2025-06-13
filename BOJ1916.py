"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

from  collections import defaultdict
import sys, heapq

# 가장 큰 두 가지
# 1. 갱신된 거리를 힙에 함께 집어넣어야 함. 힙에는 출발지로부터 고려해
# 처리한 거리와 노드가 들어감
# 2. 이미 처리한 노드는 무시.

def solve(graph: list, n: int, start: int, end: int):
    heap = []
    distances = [float('inf') for _ in range(n + 1)]
    distances[start] = 0
    heapq.heappush(heap, (0, start)) # 그냥 출발지를 넣어야 함.
    while heap:
        current_distance, u = heapq.heappop(heap)
        if current_distance > distances[u]:
            continue
        for w, v in graph[u]:   
            new_distance = distances[u] + w
            if distances[v] > new_distance:
                heapq.heappush(heap, (new_distance, v))
                distances[v] = new_distance
    print(distances[end])

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())
    graph = defaultdict(list)
    for _ in range(m):
        u, v, w = tuple(map(int, input().split()))
        graph[u].append((w, v))
    s, e = tuple(map(int, input().split()))
    # print(graph)
    solve(graph, n, s, e)
