"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

import sys

def matrix_chain_order(p, n):
    # 그럼 뭘 해? new array
    m = [[0 for _ in range(n)]for _ in range(n)]
    # 자기 자신만 곱하는 경우 초기화
    for i in range(n):
        m[i][i] = 0
    # 이 아래부터 i < j
    for l in range(2, n+1): #배열의 각 길이. 짧은 경우부터 이터레이션
        for i in range(0, n-l+1):
            # 대체 뭘 구하는 거야? i가 어디까지 커져야 하는지.
            # n - l 이러면? i = n - L - 1
            # 그러면 j는 어떻게 정의해? 
            # i + l - 1 = n 이려면? 
            # i = n - l + 1까지 커질 수 있음.
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i][0] * p[k][1] * p[j][1]
                if q < m[i][j]:
                    m[i][j] = q
    return m[0][n-1]

def test():
    n = 3
    p = [(5, 3), (3, 2), (2, 6)]
    assert matrix_chain_order(p, n) == 90 

def submit(matrix_chain_order):
    input = sys.stdin.readline
    n = int(input().strip())
    p = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    print(matrix_chain_order(p, n))

if __name__ == '__main__':	
    submit(matrix_chain_order)
    # test()
