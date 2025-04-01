"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드


4. 코드 구현
"""

import sys
input = sys.stdin.readline
A, B, C = tuple(map(int, input().split()))

def loop_power(a: int, b: int):
    result = 1
    a = a%C
    while b > 0:
        if b%2 == 1:
            result *= a%C
            print(f'result: {result} = {result} * {a} % {C}')
        print(f'{(a*a)%C} = ({a} * {a})%{C}')
        a = (a*a)%C
        b //= 2
    return result

print(loop_power(A, B))

"""
이슈: 틀렸습니다.

Phase1.
환경: 파이썬
로그: 
최근 변경 사항: 

Phase2.
확인: 
시도: 
분석: 
"""