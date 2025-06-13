"""
1. 문제 읽기
2. 문제 풀기
important thing is that the dp is not about filling the table. 
it's about doing recursion in a delicate way.
3. 수도 코드
4. 코드 구현
"""

import sys

def recur(n, k, stuffs: list):
    dp = [[0 for _ in range(n)] for _ in range(k+1)] # 가로: 물건, 세로: 무개
    # 0번째 물건에 대해
    for i in range(k+1):
        dp[i][0] = stuffs[0][1] if i >= stuffs[0][0] else 0
    # go dp
    for i in range(k+1):
        for j in range(1, n):
            if i >= stuffs[j][0]:
                dp[i][j] = max(dp[i][j-1], dp[i-stuffs[j][0]][j-1] + stuffs[j][1])
            else:
                dp[i][j] = dp[i][j-1]
    # for d in dp:
    #     print(d)
    return dp[k][n-1]

if __name__ == '__main__':	
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    stuffs = [
        tuple(map(int, input().split())) 
        for _ in range(n)
    ]
    print(recur(n, k, stuffs))


"""
4 7
6 13
4 8
3 6
5 12
"""