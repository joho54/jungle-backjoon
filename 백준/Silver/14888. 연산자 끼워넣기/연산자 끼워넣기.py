#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14888                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14888                          #+#        #+#      #+#     #
#    Solved: 2025/03/29 11:31:02 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
주어진 숫자 순서대로 노드고 
각 숫자의 순서대로 순회하는 그래프 탐색?

2. 문제 풀기
연산자가 버텍스인가? 버텍스 탐색 순서만 정해지면 연산 때리면 되잖슴. 그러네

3. 수도 코드
4. 코드 구현
""" 

import sys

def dfs(op_list: list, current_val: int, num_idx: int):
    global max_ans, min_ans
    if len(op_list) == n-1: # 모든 연산을 끝냈다면
        max_ans = max(max_ans, current_val)
        min_ans = min(min_ans, current_val)
        return
    for i in range(len(visited)):
        if visited[i] > 0:
            op_list.append(i)
            visited[i] -= 1
            result = mapper[i]((current_val, A[num_idx]))
            # print(f'{current_val, mapper2[i], A[num_idx]} = {result}')
            # print(result)
            dfs(op_list, result, num_idx+1)
            visited[i]+= 1
            op_list.remove(i)


if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    A = tuple(map(int, input().split()))
    ops = list(map(int, input().split()))
    mapper = {0: lambda x: x[0]+x[1], 
              1: lambda x: x[0]-x[1], 
              2: lambda x: x[0]*x[1], 
              3: lambda x: x[0]//x[1] if x[0] > 0 else -(-x[0]//x[1])}
    # mapper2 = {0: '+', 
    #           1: '-', 
    #           2: '*', 
    #           3: '/'}
    # print(ops)
    # print(A)
    max_ans = -sys.maxsize
    min_ans = sys.maxsize
    for i in range(len(ops)): # 각각의 시작점에 대해
        # 아 알거 같기도 하고 모르겠네. 일단 연산자 쌍을 출력하는 거를 만들어 볼가.
        # copy?
        visited = ops.copy()
        result = 0
        if ops[i] > 0: #연산자를 쓸 수 있다면
            visited[i] -= 1 # 1 빼고
            result = mapper[i]((A[0], A[1])) # 최초 연산을 한 다음
            dfs([i], result, 2) # dfs로 넘기기.
    print(max_ans )
    print(min_ans)


## n 최대값이 11이므로 브루트포스 매우 가능함.