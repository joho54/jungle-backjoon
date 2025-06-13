
parents = []

def union(u: int, v: int):
    parents[u] = v

def find(u: int):
    if (parents[u] != u):
        parents[u] = find(parents[u])
    return parents[u]

