#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11724                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11724                          #+#        #+#      #+#     #
#    Solved: 2025/03/28 17:21:49 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

def bfs(root: int):
    que = deque() # 큐 정의
    que.appendleft(root) # 루트 어펜드
    
    while que: # 큐가 존재하는 동안
        # u = E[que.pop()] # 들어간 노드가 갈 수 있는 노드를 확인
        for u in E[que.pop()]:
            if not is_visited[u]: # 그 노드가 방문되지 않았다면
                is_visited[u] = True # 방문 실시
                que.appendleft(u)

import sys
from collections import deque, defaultdict

if __name__ == '__main__':	
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    arr = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    # E = defaultdict() # 간선이 하나밖에 없어도 버텍스의 차수가 여럿일 수 있어서 리스트 필요
    E = {
        i: [] for i in range(1, n+1)
    }
    # print(E)
    # print(arr)
    for u, v in arr:
        # print(u, v)
        E[u].append(v)
        E[v].append(u)
    is_visited = [False for _ in range(n+1)] # V + 1
    cnt = 0
    # print(E)
    for v in range(1, n+1): # 모든 버텍스에 대해 순회
        if not is_visited[v]: # 실행 시점에 방문되지 않았다면
            # print(f'{v} is not traveled') # 방문 실시
            cnt += 1
            is_visited[v] = True #
            bfs(v)
    print(cnt)
        