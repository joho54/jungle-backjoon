#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9084                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9084                           #+#        #+#      #+#     #
#    Solved: 2025/04/04 10:22:45 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def recur(n: int, coins: list, max_coin_idx: int):
    pass

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
        


"""
3
2
1 2
1000
3
1 5 10
100
2
5 7
22
"""