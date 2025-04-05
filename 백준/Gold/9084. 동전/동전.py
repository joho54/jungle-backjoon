import sys

if __name__ == '__main__':	
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        m = int(input().strip())
        coins = tuple(map(int, input().split()))
        n = int(input().strip())
        dp = [[0 for _ in range(m)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m):
                if i - coins[j] == 0:
                    dp[i][j] = 1
                else:
                    tmp = 0
                    for k in range(0, j+1):
                        if i-coins[j] >= 0:
                            tmp += dp[i-coins[j]][k]
                    dp[i][j] = tmp
        print(sum(dp[n]))