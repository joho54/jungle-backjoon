# 문제: b가 작은 값만 나옴.

import sys, math

def solve(a: int):
    cnt = 0
    for x in range(1, a):
        # x가 먼저 a제곱의 약수인지 확인하기
        a_square = a**2
        if a_square % x == 0:
            # a_square의 x의 몫 y 구하기(// 연산자를 써도 괜찮은 이유: y는 무조건 자연수임이 보장되므로 소수점 값이 없음)
            y = a**2 // x
            b = (y-x)/2 # b는 자연수가 아닐 수도 있음. 우선 float 타입으로 결과값을 받고 is_integer() 연산자로 확인
            if b.is_integer() and  b > a:
                cnt += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.readline
    while True:
        n = int(input().strip())
        if n == 0:
            break
        print(solve(n))