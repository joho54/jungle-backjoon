"""
1. 문제 읽기
2. 문제 풀기
MST를 구한 후 그 중에서도 가장 큰 가중치의 간선을 하나 없애면 됨.
3. 수도 코드
4. 코드 구현
"""

import sys
sys.setrecursionlimit(10**8)

parents = []
rank = []

def union(x: int, y: int): 
    global parents
    x = find(x)
    y = find(y)
    if y != x:
        # Union by rank
        if rank[x] < rank[y]:  # x의 랭크가 y보다 작다면
            parents[x] = y # x의 부모를 y로 지정.
        else: # x의 랭크가 y보다 같거나 크다면
            parents[y] = x # y의 부모를 x로 지정.
            if rank[x] == rank[y]: # 만약 두 랭크가 동일했다면
                rank[x] += 1 # x의 랭크를 1 올려줌.
        return True
    return False

def find(x: int):
    global parents
    if x != parents[x]:
        x = find(parents[x])
    return x

# def done_check():
#     global parents
#     a = parents[1]
#     for i in range(2, len(parents)):
#         if a != parents[i]: return False
#     return True

# 최적화 안 된게 문제다.

def solve(n: int, m: int, E: list):
    global parents, rank
    # 루트를 자기 자신으로 초기화
    parents = [i for i in range(n+1)]
    # 각 노드를 순회하면서 압축
    # 완성된 그래프에서 가장 큰 가중치를 빼야 함.
    mst = []
    weight_sum = 0
    edge_count = 0
    rank = [1]*(n+1) # 랭크를 1로 초기화.
    for u, v, w in E: # 이 값이 엄청 큼.
        is_merged = union(u, v)
        if is_merged: # 압축이 발생했으면
            mst.append((u, v, w))
            weight_sum += w
            edge_count += 1
        if edge_count == n-1:  # MST 완성 시 조기 종료
            break
    # 어차피 mst는 가중치 순으로 정렬됨.
    weight_sum -= mst[-1][2]
    return weight_sum

if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = tuple(map(int, input().split()))
    E = []
    for _ in range(m):
        u, v, w = tuple(map(int, input().split()))
        E.append((u, v, w))
    E.sort(key = lambda x: x[2])

    print(solve(n, m, E))