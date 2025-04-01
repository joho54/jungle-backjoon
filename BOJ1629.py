"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드

result *= a%C
4. 코드 구현
"""

import sys
input = sys.stdin.readline
A, B, C = tuple(map(int, input().split()))

def power(a: int, b: int):
    # print(f'a: {a}, b: {b}. so {a}^{b}')
    if b == 1: return a%C
    # print(f'get temp: power({a}, {b//2})%{C}', end=' ')
    temp = power(a, b//2)%C
    # print(f'temp = {temp}')

    if b%2 == 0: 
        # print(f'b is even. ({temp}*{temp})%{C}')
        return (temp*temp)%C
    else:
        # print(f'b is odd. {temp}*{temp}*{a} % {C} = {(temp*temp*a)%C}') 
        return (temp*temp*a)%C

def loop_power(a: int, b: int):
    result = 1
    while b > 0:
        result *= a%C
        if b%2 == 1: 
            result *= a
        a = a*a 
        b //= 2
    print(result)

print(loop_power(A, B))

"""
이슈: 틀렸습니다.

Phase1.
환경: 파이썬
로그: 찍어보세요
최근 변경 사항: power 구현

Phase2.
확인: 
10 11 12
a: 10, b: 11. so 10^11
get temp: power(10, 5)%12 a: 10, b: 5. so 10^5
get temp: power(10, 2)%12 a: 10, b: 2. so 10^2
get temp: power(10, 1)%12 a: 10, b: 1. so 10^1
temp = 10
b is even. (10*10)%12
temp = 4
b is odd. 4*4*10 % 12 = 4
temp = 4
b is odd. 4*4*10 % 12 = 4
4

시도: 로그하고는 별 상관 없었는데, base case에서 b==0으로 돼 있었음.
분석: 성공.
그런데 왜 b==0이면 안 되고 b==1이면 되는 거지? 직전 재귀에서 b가 짝수면 1일 거고, 홀수면
0이겠지. 왜 홀수에서 분기한 재귀는 고려하지 않아도 되는 거지? 납득이 안 됨.(혼자 힘으로 생각해보기)
아, 어떤 수//2=0으로 만들어버리는 경우는 1 말고는 없기 때문이다. 1//2 연산을 한 다음 재귀로 갈 일이 없기 때문에
(바닥 케이스에서 걸리기 때문에) 0은 고려하지 않아도 되는 거다.
"""