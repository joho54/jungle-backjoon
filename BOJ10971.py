# 문제 쉐도잉.
# 어 이거 그냥 BFS 아닌가. 
# 출발은 어디서? 아무데서. 이 부분에서 완전탐색을 해야함.
# 아 기억 안 나는데 일단 함수 세개가 필요함
# dfs로 풀어야 하나?  스택에다가 갈 지역을 집어넣고, 비용이 최소인 것을 차례로 올려보내서 한 지역에서 갈 수 있는 최소값을 구하면 되나? 
# i, j가 직관적이지가 않네.
# 그래프 쓰면 DFS를 쓸 수 있을 거 같은데 아직 머리에 개념이 잘 안 잡혀서 패스. n이 최대 10이므로 진짜 완전탐색 해도 될 거 같기도? 
# n by n이라 복잡도가 n^2^2처럼 느껴질수도 있지만, 1 -> 2 -> 3 -> ... -> n 이렇게 선형 순회하는 거라 n^2이면 충분할듯.
# 문제 다시 읽기.
# 아아아아 다시 이해했다. 돌아서 결국 돌아오는 거잖아. 왔던 길이 아니라.

import sys
MAX_INT = sys.maxsize
min_cost = MAX_INT

def visit_to(i, cost, log: list): 
    global min_cost, home
    if not False in flag_visit: # 바닥조건 다시 생각하기. 갔던 마을로 다시 갈 수는 없으니까 결국 마지막 방문한 마을에서 원래 마을로 돌아오는 값을 더해야 함.
        if costs[i][home] != 0:
            min_cost = min(min_cost, cost+costs[i][home]) 
        return
    for j in range(n):
        if flag_visit[j] == False and costs[i][j] != 0: 
            flag_visit[j] = True
            visit_to(j, cost + costs[i][j], [*log, j])
            flag_visit[j] = False

n = int(input())

flag_visit = [
    False
    for _ in range(n)
]

costs = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

for i in range(n):
    flag_visit[i] = True
    home = i
    for j in range(n):
        if costs[i][j] != 0:
            flag_visit[j] = True
            visit_to(j, costs[i][j], [i, j]) 
            flag_visit[j] = False
    flag_visit[i] = False

print(min_cost)
