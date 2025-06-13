#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1388                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1388                           #+#        #+#      #+#     #
#    Solved: 2025/04/03 10:03:54 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
dx, dy 써서 잘 하면 될듯. 일단 옆으로 좀 가ㅁㅇㄹㅁ아
3. 수도 코드
4. 코드 구현
"""

import sys
from collections import deque
# 오른쪽이나 아래로만 가면 됨. visited면 건너 뛰고
dxs, dys = [0, 1], [1, 0]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def search_floor():
    # 먼저 시작지점에서 출발
    visited = [[False for _ in range(m)] for _ in range(n)]
    # queue = deque(start)
    cnt = 0
    # 완탐 하면서
    for i in range(n):
        for j in range(m):
            # 만약 해당 타일이 방문되지 않았다면
            # 오른쪽, 아래쪽 방향으로 탐색하고
            if not visited[i][j]:
                # 올려주고.]
                visited[i][j] = True
                cnt += 1
            if i+1 < n and floor[i][j] == floor[i+1][j] == '|':
                visited[i+1][j] = True
            if j+1 < m and floor[i][j] == floor[i][j+1] =='-':
                visited[i][j+1] = True

            # 이미 방문했으면 인접한 친구들만 업데이트 해줘야 함.
    return cnt


if __name__ == '__main__':	
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    floor = [
        list(input().strip())
        for _ in range(n)
    ]
    # print(n, m, floor)
    cnt = search_floor()
    print(cnt)