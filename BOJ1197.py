


def union(u: int, v: int, parents: list):
    root_u = find(u, parents)
    root_v = find(v, parents)
    if root_u != root_v: # 조건 추가. 
        parents[root_u] = root_v

def find(u: int, parents: list):
    if (parents[u] != u):
        parents[u] = find(parents[u], parents)
    return parents[u]

import sys

def solve(E: list, v: int):
    # make set
    parents = [ i for i in range(v+1)]
    # sort the edges
    E.sort()
    # set A
    a = []
    # for each edge
    for w, u, v in E:
        if find(u, parents) != find(v, parents):
            a.append((w, u, v))
            union(u, v, parents)
    return a

def sum_weights(a: list):
    ans = 0
    for w, _, _ in a:
        ans += w
    return ans


if __name__ == '__main__':	
    input = sys.stdin.readline
    v_, e = tuple(map(int, input().split()))
    E = []
    for i in range(e):
        u, v, w = tuple(map(int, input().split()))
        E.append((w, u, v))
    print(sum_weights(solve(E, v_)))