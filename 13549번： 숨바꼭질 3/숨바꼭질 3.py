#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13549                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13549                          #+#        #+#      #+#     #
#    Solved: 2025/04/02 14:09:41 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    maze = [
        tuple(map(int, list(input().strip())))
        for _ in range(n)
    ]
    for m in maze:
        print(m)