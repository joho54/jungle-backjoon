#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 21606                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/21606                          #+#        #+#      #+#     #
#    Solved: 2025/03/28 21:44:55 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
그냥 모든 버텍를 루트로 dfs 돌리면 되는 거 같은데

3. 수도 코드
4. 코드 구현
"""

import sys

def dfs(root: int):
    global cnt
    v = root
    for u in E[v]:
        if not visited[u] and A[u-1] != 1: # not visited and not inside
            visited[u] = True
            dfs(u)
        elif not visited[u] and A[u-1] == 1: # not visited and inside
            cnt += 1


if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    # 버텍스를 딕셔너리로 관리해야 하나?
    A = tuple(map(int, tuple(input().strip()))) # idx - 1로 접근
    arr = [
        tuple(map(int, input().split()))
        for _ in range(n-1)
    ]
    E = {
        i:[] for i in range(n+1)
    }
    for v, u in arr:
        E[v].append(u)
        E[u].append(v)
    # is_inside = {} # V[vertex val] = 0 or 1
    # for idx, a in enumerate(A, 1):
    #     is_inside[idx] = a
    # print(is_inside)
    cnt = 0
    for v in range(1, n+1):
        if A[v-1] == 1: # 출발은 실내에서
            visited = [False for _ in range(n+1)]
            # print(f'starting: {v}')
            visited[v] = True
            dfs(v)
    print(cnt)