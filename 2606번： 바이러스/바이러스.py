#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2606                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2606                           #+#        #+#      #+#     #
#    Solved: 2025/03/28 17:47:28 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

def bfs(root: int):
    que = deque()
    que.appendleft(root)
    is_visited = [False for _ in range(n+1)]
    cnt = 0
    while que:
        v = que.popleft()
        for u in E[v]:
            if not is_visited[u]:
                is_visited[u] = True
                que.appendleft(u)
                cnt += 1
    return  cnt

if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())
    network = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    E = {
        i:[] for i in range(n+1)
    }
    for u, v in network:
        E[u].append(v)
        E[v].append(u)
    result = bfs(1)-1 
    result = result if result >= 0 else  0
    print(result)
