"""
1. 문제 읽기
유니언 파인드와 탐색을 결합한 문제임.
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

from collections import defaultdict
import sys

def pre_order(graph: defaultdict, visited: list, node: int):
    visited[node] = True
    print(node)
    for next_node in graph[node]:
        if not visited[next_node]:
            pre_order(graph, visited, next_node)

def submit(pre_order):
    input = sys.stdin.readline
    arr = tuple(map(int, input().split()))
    graph = defaultdict(list)
    # make graph --need graph number
    for u, v in arr[1:]:
        graph[u].append(v)
        graph[v].append(u)
    pre_order(1)

def test():
    arr = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)]
    graph = defaultdict(list)
    visited = [False for _ in range(6)]
    for u, v in arr[1:]:
        graph[u].append(v)
        graph[v].append(u)
    pre_order(graph, visited, 1)

if __name__ == "__main__":
    # submit(pre_order)
    test()
    
    
