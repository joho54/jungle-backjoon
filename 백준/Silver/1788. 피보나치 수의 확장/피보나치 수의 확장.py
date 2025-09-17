# label: DP

import sys

MODULO =  1_000_000_000

def fibo(n: int):
    assert n >= 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2])%MODULO
    return dp[n]

def fibo_minus(n: int):
    if n == 0: 
        return 0
    elif n == -1:
        return -1
    n = abs(n)
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-2] - dp[i-1])  % MODULO + MODULO
    return dp[n]

def solve(n: int):
    if n >= 0:
        # 일반적인 dp 풀이
        ans = fibo(n)
        sign = 1
        if ans == 0:
            sign = 0
            
        return sign,  ans % MODULO
    elif n < 0: 
        ans = fibo_minus(n)
        sign = 1
        if ans < 0: sign = -1
        elif ans == 0: sign = 0
        return sign, abs(ans) % MODULO

def fibo_dp(n: int):
    dp = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MODULO
    return dp[n]

def solve2(n: int):
    if n == 0:
        return 0, 0
    abs_n = abs(n)
    fib = fibo_dp(abs_n)
    if n > 0:
        sign = 1
    else:
        sign = 1 if abs_n % 2 == 1 else -1  # F(-n) = (-1)^{n+1} F(n)
    return sign, fib

# 입력, 출력 부분은 동일


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    sign, ans = solve2(n)
    

    print(sign)
    print(ans)