import sys
import math

input = sys.stdin.readline

n, b = map(int, input().split())
sum_x, sum_y = 0, 0
for _ in range(n):
    x, y = map(int, input().split())
    sum_x += x
    sum_y += y

numerator = sum_y - n * b
denominator = sum_x

if denominator == 0:
    print("EZPZ")
else:
    # 약분
    gcd = math.gcd(abs(numerator), abs(denominator))
    p = numerator // gcd
    q = denominator // gcd
    # 양의 분모로 통일
    if q < 0:
        p = -p
        q = -q
    # 정수라면 정수로 출력
    if q == 1:
        print(p)
    else:
        print(f"{p}/{q}")
