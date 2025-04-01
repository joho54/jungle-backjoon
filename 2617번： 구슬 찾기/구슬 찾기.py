#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2617                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2617                           #+#        #+#      #+#     #
#    Solved: 2025/03/29 15:14:50 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기

4 > 2 > 1
  > 3
5 > 1
4번은 안 된다. 왜? 자기보다 가벼운 구슬이 3개 있으므로((n+1)//2)개 이상 있으므로
1번도 안 된다. 자기보다 무거운게 2, 4, 5로 똑같이 3개 이상 있음.

2 1
4 3
5 1
4 2

각 구슬에 dfs한 다음 depth > ((n+1)//2)이상이 되면 false 하면 되겠네

3. 수도 코드
4. 코드 구현
"""

import sys

def dfs_lighter(v: int):
    global l
    visited[v] = True
    for u in lighter[v]:
        if not visited[u]:
            # print(f'lighter: {v} -> {u}')
            l += 1
            dfs_lighter(u)

def dfs_heavier(v: int):
    global h
    visited[v] = True
    for u in heavier[v]:
        if not visited[u]:
            # print(f'heavier: {v} -> {u}')
            h += 1
            dfs_heavier(u)

if __name__ == '__main__':	
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    arr = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]

    lighter = {
        i: [] for i in range(n+1)
    }
    heavier = {
        i: [] for i in range(n+1)
    }
    for v, u in arr:
        lighter[v].append(u)
        heavier[u].append(v)
    cnt = 0
    for v in range(1, n+1):
        visited = [False for _ in range(n+1)]
        l, h = 0, 0
        dfs_lighter(v)
        dfs_heavier(v)
        # print(f'l: {l}, h: {h}')
        if l >= (n+1)//2 or h >= (n+1)//2:
            cnt += 1
    print(cnt)

"""
이슈: depth 만 체크하면 서로 이어지지 않은 버텍스를 탐지할 수 없음. 
그렇다고 heavier, lighter를 각각 해서 하나의 dfs에서 처리하면 당연히 꼬임.
그럼? dfs함수 두개 만ㄷ르면 안 되나?

Phase1.
환경: 파이썬
로그: 
최근 변경 사항: 

Phase2.
확인: 
시도: 
분석: 
"""