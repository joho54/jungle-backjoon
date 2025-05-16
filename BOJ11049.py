"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

import sys
from collections import defaultdict

def get_cost(n: int, m: int, k: int):
    return n * m * k

def recur(matrices: list, memo = defaultdict(tuple)):
    # 행렬들 matrices의 최소 연산 비용을 반환한다.
    if len(matrices) <= 1: return 0
    # 첫 번째 행렬만 단독으로 나머지와 연산할 경우를 위해
    head = matrices[0]
    n, m1 = head[0], head[1]
    rest = matrices[1:] 
    k = rest[-1][1]
    memo[(m1, k)] = recur(rest, memo)
    cost1 = get_cost(n, m1, k) + memo[(m1, k)]
    # 두 번째 행렬과 함께 연산할 경우를 위해 
    cost2 = sys.maxsize
    if len(matrices) > 2:
        head = matrices[0:2]
        rest = matrices[2:]
        m2 = head[1][1]
        k = rest[-1][1]
        memo[(m2, k)] = recur(rest, memo)
        cost2 = get_cost(n, m2, k) + memo[(m2, k)]
    memo[(n, k)] = min(cost1, cost2)
    return memo[(n, k)]

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().strip())
    matrices = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    memo = defaultdict()
    recur(matrices=matrices, memo=memo)
    
    print(memo)
