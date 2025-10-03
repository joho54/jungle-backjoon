import sys
from collections import defaultdict, deque

# 혈통을 기록하긴 해야함.
def topo_sort(graph: defaultdict, king: str): 
    indegree = {u:0 for u in graph}
    blood = {u:0 for u in graph}
    blood[king] = 1
    # set indegree
    for key in graph:
        for child in graph[key]:
            indegree[child] += 1
            assert indegree[child] <= 2
    # print(indegree)
    # set queue
    queue = deque()
    sorted_keys = []
    for key in graph:
        if indegree[key] == 0: # 얘네는 부모가 없고 그냥 내적이 0인 노드들이라서 혈통이 당연히 0임
            queue.append(key)
            sorted_keys.append(key)
    # topo sort
    while queue:
        u = queue.popleft() # 팝과 동시에 정렬 배열에 추가
        for v in graph[u]: # 자식 순회하면서 내적 감소
            indegree[v] -= 1 # 이때 자식에게 기록해야 함.
            blood[v] += blood[u] # 부모 혈통 기록
            # print(f'{u, blood[u]} -+-> {v, blood[v]}')
            if indegree[v] == 0: # 내적이 0이 되면 큐에 추가
                sorted_keys.append(v)
                queue.append(v)
                # 큐에 더해지는 시점에 혈통 정산
                blood[v] /= 2
                # print(f'final: {v, blood[v]}')
    return sorted_keys, blood
                

def solve(n: int, m: int, king: str, graph: defaultdict, candidates: set):
    sorted_keys, blood = topo_sort(graph, king)
    # print(sorted_keys)
    # print(blood)
    next_king = None
    for candidate in candidates:
        if not next_king:
            next_king = candidate
        elif blood[candidate] > blood[next_king]: #update
            next_king = candidate
    return next_king
            
        

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    king = input().strip()
    arr = [
        tuple(map(str, input().split()))
        for _ in range(n)
    ]
    candidates = {
        input().strip()
        for _ in range(m)   
    }
    graph = defaultdict(list)
    # key가 고유명사이므로 키를 초기화할 필요가 있음. 
    for u, v, w in arr:
        graph[u] = []
        graph[v] = []
        graph[w] = []
    for u in candidates:
        graph[u] = []
    for u, v, w in arr: # v, w are parent
        graph[v].append(u)
        graph[w].append(u)
    print(solve(n, m, king, graph, candidates))
    
