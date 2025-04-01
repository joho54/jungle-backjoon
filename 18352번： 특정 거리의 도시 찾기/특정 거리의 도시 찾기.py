#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18352                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18352                          #+#        #+#      #+#     #
#    Solved: 2025/03/29 10:34:11 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
1. 문제 읽기
2. 문제 풀기
미로 문제와는 그래프 입력이 다름. 딕셔너리를 사용한 인접리스트를 구현해야 함.
3. 수도 코드
4. 코드 구현
"""

import sys
from collections import deque

def bfs(root: int):
    que = deque()
    que.appendleft(root)
    visited = [-1 for _ in range(n+1)]
    visited[root] = 0
    ans = []
    while que:
        v = que.pop()
        # print(v)
        for u in E[v]:
            # print(f'u: {u}')
            if visited[u] == -1:
                visited[u] = visited[v]+1
                if visited[u] == k:
                    ans.append(u)
                que.appendleft(u)
    return sorted(ans)




if __name__ == '__main__':	
    input = sys.stdin.readline
    n, m, k, x = tuple(map(int, input().split()))
    E = {
        i: [] for i in range(n+1)
    }
    arr = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    for v, u in arr:
        E[v].append(u)
    result = bfs(x)
    if result:
        for r in result:
            print(r)
    else:
        print(-1)