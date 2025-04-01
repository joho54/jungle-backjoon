#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1707                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1707                           #+#        #+#      #+#     #
#    Solved: 2025/03/28 20:24:35 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

import sys
sys.setrecursionlimit(10**8)

def dfs(v: int, color: int):
    global flag
    visited[v] = color
    for u in E[v]:
        if visited[u] != -1:
            if visited[v] == visited[u]: # 0 == 0 or 1 == 1
                flag = True
                return 
        else: 
            visited[u] = color
            dfs(u, 1-color)

if __name__ == '__main__':	
    input = sys.stdin.readline
    k = int(input().strip()) 
    for _ in range(k):
        v, e = tuple(map(int, input().split()))
        E = {
            i: [] for i in range(v+1)
        }
        arr = [
            tuple(map(int, input().split()))
            for _ in range(e)
        ]
        for u, v_ in arr:
            E[v_].append(u)
            E[u].append(v_)
        visited = [-1 for _ in range(v+1)]
        flag = False
        # edge가 없을 수도 있자나!
        for v in E.keys():
            if visited[v] == -1:
                dfs(v, 0)
        out = 'NO' if flag else 'YES'
        print(out)
"""
이슈: 틀렸습니다.

Phase1.
환경: 파이썬
로그: 
최근 변경 사항: 그냥 사이클이 없으면 틀린 걸로 판단하는 dfs 함수를 짰는데, 그냥 문제 이해를 
잘못 한 거일수도? 그러네. 어쨌든 사이클 검사하는 함수는 제대로 썼잖아. 한잔해~
그리고 다시 생각해보니, 사이클을 이루는 버텍스 수가 홀수면 안 된다. 
사이클 수를 측정하는 방법은 없나?

Phase2.
확인: color이라는 걸 만들어서 서로 사이클을 형성하는 노드의 번호 차가 짝수면 이분 트리 아닌 걸로 시도
시도: 
for u in E[v]:
    if visited[u] == True: #이걸로는 사이클 확인 불가
        # 왜? 무방향 그래프에서는 온 길도 True로 보게 됨.
        # 그럼 출발하기 전에 없애버리면 안 되나.
        # print(f'already visited {u}')
        # print(f'count map. {color[v]} meets {color[u]}')
        if (color[v] - color[u])%2 == 0:
            return False
    else: # not true
        # print(f'exploring {u}, {E[u]}, {v}')
        # 이렇게.
        E[u].remove(v)
        visited[u] = True
        return dfs(u, cnt+1)
분석
실패.

"""

"""
이슈: 피드백 반영해서, 순회하며 색을 직접 탐색하는 방법으로 처리. 46프로에서 오답 발생

Phase1.
환경: 파이썬
로그: 
최근 변경 사항: 

Phase2.
확인: 뭘 확인해야 함? 46프로에서 틀리는데... 하 진짜 뭐가 문제지. 
시도: 
분석: 
"""