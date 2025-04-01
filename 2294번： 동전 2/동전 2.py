#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2294                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2294                           #+#        #+#      #+#     #
#    Solved: 2025/03/30 14:16:16 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
워낙 많이 풀어 봤던 그거라서. 기억을 더듬어 풀어 봅시다.
dp[n] = min(dp[n-A[0~]] + 1)
3. 수도 코드
4. 코드 구현
"""

import sys
INF = sys.maxsize


def make_dp():
    dp[0] = 0
    for i in range(1, k+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin]+1)


if __name__ == '__main__':	
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    coins = [
        int(input().strip())
        for _ in range(n)
    ]
    # init
    dp = [INF for _ in range(k+1)]
    make_dp()
    # print(dp)
    result = dp[k] if dp[k] != INF else -1
    print(result)