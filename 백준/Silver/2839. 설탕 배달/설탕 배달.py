import sys

def solve(n: int) -> int:
    # init dp
    dp = [-1] * (n + 1)
    
    dp[0] = 0
    
    # -1을 채울 생각 하지 말고, 0, 혹은 그 이상의 숫자를 채울 생각을 해야지
        
    # calculate dp
    for i in range(1, n+1):
        if i >= 3 and dp[i-3] != -1:
            dp[i] = dp[i-3] + 1
        if i >= 5 and dp[i-5] != -1:
            if dp[i] == -1 or dp[i-3] > dp[i-5]:
                dp[i] = dp[i-5] + 1
                

    # return answer
    return dp[n]
        

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().strip())
    
    print(solve(n))