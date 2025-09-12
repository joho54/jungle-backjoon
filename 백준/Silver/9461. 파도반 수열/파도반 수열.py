""" 1 1 1 2 2 3 4 5 7 9 13

2[3] = [0] + [2]
2[4] =       [3]
3[5] = [2] + [4]
4[6] = [1] + [5]
5[7] = [0] + [6]

7[8] = [3] + [7]
9[9] = [4] + [8]
12[10] = [5] + [9] """

# 라벨: 수학+DP

import sys

def solve(n: int):
    # dp set
    dp = [0 for _ in range(n+1)]
    # dp init
    init_dp = [0, 1, 1, 1, 2, 2, 3, 4, 5]
    init_limit = min(n+1, len(init_dp))
    for i in range(init_limit):
        dp[i] = init_dp[i]
    for i in range(init_limit, n+1):
        dp[i] = dp[i-5] + dp[i-1]
    return dp[n]

if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(solve(n))