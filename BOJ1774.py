"""
1. 문제 읽기
2. 문제 풀기
뭘 어떻게 풀면 되지? 거리가 일단 없다는 점.
3. 수도 코드
4. 코드 구현
"""

import sys
import math

parents = []

def get_graph(grid: list, A: set, n: int):
    # 모든 노드를 순회하면서 두 노드 사이의 거리를 계산.
    graph = []
    for i in range(1, n+1):
        for j in range(i+1, n+1): 
            if (i, j) in A: # 두 노드가 이미 연결됐다면
                graph.append((0, i, j))
            # 두 노드가 연결되지 않았다면
                
            else:
                x_len = grid[i][0] - grid[j][0]
                y_len = grid[i][1] - grid[j][1]
                dist = math.hypot(x_len, y_len)
                graph.append((dist, i, j)) # 두 노드 사이의 거리를 계산해서 추가.
    return graph

def find(x: int):
    global parents
    if x != parents[x]:
        x = find(parents[x])
    return x

def union(x: int, y: int):
    global parents
    xr = find(x)
    yr = find(y)

    if xr != yr:
        if ranks[xr] > ranks[yr]: # xr의 높이가 yr보다 높다면, 작은 yr을 병합
            parents[yr] = xr # xr의 부모는 yr이다.
        else:
            parents[xr] = yr # 일단 병합하고
            if ranks[xr] == ranks[yr]:
                ranks[yr] += 1
        return True
    else: 
        return False


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    parents = [i for i in range(n + 1)] # 부모 초기화.
    ranks = [1 for _ in range(n+1)] # rank 초기화
    grid = [(None, None)] # set with sentinel 
    for _ in range(n):
        grid.append(tuple(map(int, input().split())))
    A = set()
    for _ in range(m):
        x, y = tuple(map(int, input().split())) # 이럴 경우 그냥 거리를 0으로 잡아야 한다.
        A.add((x, y))
        A.add((y, x))
    graph = get_graph(grid, A, n)
    # print(graph) # 그래프가 잘 나오는지 확인
    # union find로 경로 압축. 및, 거리가 0이 아닌 경우 해당 거리를 결과에 추가.
    # 간선을 정렬
    graph.sort(key=lambda x: x[0]) # 가중치 순으로 간선 정렬
    result = 0
    for w, u, v in graph: # 가중치 순으로 정렬된 그래프 순회
        is_merged = union(u, v) # u, v를 병합. 만약 병합이 일어났으면 가중치를 결과에 추가.
        if is_merged:
            result += w
    print(f'{result:.2f}')
    


""" 
4 1
1 1
3 1
2 3
4 3
1 4

 """