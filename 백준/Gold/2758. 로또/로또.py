import sys

def solve(n: int, m: int):
    dp = [
        [0 for _ in range(m+1)]
        for _ in range(n+1)
    ]
    for j in range(m+1):
        dp[1][j] = 1
        
    # row 0, column 0 are not used
    for i in range(n+1):
        dp[i][0] = 0
    for j in range(m+1):
        dp[0][j] = -1
    
    for i in range(2, n+1):
        for j in range(1, m+1):
            target = j//2
            if dp[i-1][target] == -1:
                dp[i][j] = -1 # 만들 수 없는 경우
            else:
                for k in range(target+1): # 여기서 더 개선할 수 있긴 하겠지. 근데 모르겠다.
                    if dp[i-1][k] != -1:
                        dp[i][j] += dp[i-1][k]
    ans = 0
    for elem in dp[-1]:
        if elem != -1:
            ans += elem
    return ans


def solve2(n: int, m: int) -> int:
    dp = [[0] * (m+1) for _ in range(n+1)]
    prefix = [[0] * (m+1) for _ in range(n+1)]

    # 길이가 1일 때: dp[1][j] = 1 (1 ≤ j ≤ m)
    for j in range(1, m+1):
        dp[1][j] = 1
    for j in range(1, m+1):
        prefix[1][j] = prefix[1][j-1] + dp[1][j]

    # 점화식
    for i in range(2, n+1):
        for j in range(1, m+1):
            dp[i][j] = prefix[i-1][j//2]
        for j in range(1, m+1):
            prefix[i][j] = prefix[i][j-1] + dp[i][j]

    return prefix[n][m]

if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n, m = tuple(map(int, input().split()))
        print(solve2(n, m))