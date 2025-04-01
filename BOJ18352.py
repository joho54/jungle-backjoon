"""
1. 문제 읽기
2. 문제 풀기
미로 문제와는 그래프 입력이 다름. 딕셔너리를 사용한 인접리스트를 구현해야 함.
3. 수도 코드
4. 코드 구현
"""

import sys
from collections import defaultdict

if __name__ == '__main__':	
    input = sys.stdin.readline
    n, m, k, x = tuple(map(int, input().split()))
    E = {
        i: [] for i in range(n+1)
    }
    arr = [
        tuple(map(int, input().split()))
        for _ in range()
    ]
    for v, u in arr:
        E[u].append(v)
    print(E)