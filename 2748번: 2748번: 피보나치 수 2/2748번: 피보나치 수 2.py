#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2748                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2748                           #+#        #+#      #+#     #
#    Solved: 2025/04/03 20:46:58 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


import sys

def fibo(n):
    arr = [0 for _ in range(n+1)]
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    print(arr[n])

if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    fibo(n)