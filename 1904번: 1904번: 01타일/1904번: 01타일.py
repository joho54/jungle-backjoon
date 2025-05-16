#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1904                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1904                           #+#        #+#      #+#     #
#    Solved: 2025/04/03 21:05:26 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

def sub_problem(n):
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    if n >= 2:
        dp[2] = 2
    for i in range(3, len(dp)):
        dp[i] = (dp[i-2] + dp[i-1])%15746
    return dp[n]

if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    print(sub_problem(n))