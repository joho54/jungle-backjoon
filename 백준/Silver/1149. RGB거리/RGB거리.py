import sys

def solve(grid: list, n: int):
    dp = [[ float('inf') for _ in range(n)] for _ in range(n)]
    # init
    for i in range(3):
        dp[0][i] = grid[0][i]
    
    for i in range(1, n):
        for j in range(3):
            # j == 0이라면, dp[i-1][1], dp[i-1][2]를 비교해야 함.
            if j == 0: 
                dp[i][j] = min(dp[i-1][1] + grid[i][j], dp[i-1][2] + grid[i][j])
            if j == 1: 
                dp[i][j] = min(dp[i-1][0] + grid[i][j], dp[i-1][2] + grid[i][j])
            if j == 2: 
                dp[i][j] = min(dp[i-1][1] + grid[i][j], dp[i-1][0] + grid[i][j])
    
    return min(dp[n-1])

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().strip())
    grid = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    print(solve(grid, n))