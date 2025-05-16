#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1931                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1931                           #+#        #+#      #+#     #
#    Solved: 2025/04/05 20:53:58 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def solve(time_table: tuple):
    cnt = 0
    prev_start = prev_end = 0, 0
    for current_start, current_end in time_table:
        if current_start >= prev_end:
            prev_start.
        


if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    time_table = []
    for _ in range(n):
        time_table.append(tuple(map(int, input().split())))
    time_table.sort(key=lambda x: x[1])
    # print(time_table)
    print(solve(time_table))