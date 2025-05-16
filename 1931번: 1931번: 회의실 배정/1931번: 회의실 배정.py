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

def solve(time_table: list):
    time_table.sort(key=lambda x: (x[1], x[0]))
    prev_start = prev_end = -sys.maxsize
    cnt = 0
    result = []
    for current_start, current_end in time_table:
        if current_start >= prev_end:
            cnt += 1
            result.append((current_start, current_end))
            prev_start, prev_end = current_start, current_end
    # print(result)
    return cnt

def test():
    time_table = [(1, 4), (4, 4), (4, 5)]
    assert solve(time_table) == 3
    time_table = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    assert solve(time_table) == 4
    time_table = [(1, 4), (1, 1), (1, 1)]
    assert solve(time_table) == 3
    time_table = [(0, 0)]
    assert solve(time_table) == 1
    time_table = [(0, 2), (5, 5), (0, 0), (5, 10), (3, 5), (6, 9)]
    assert solve(time_table) == 5


if __name__ == '__main__':	
    ###########################
    input = sys.stdin.readline
    n = int(input().strip())
    time_table = []
    for _ in range(n):
        time_table.append(tuple(map(int, input().split())))
    print(solve(time_table))
    ###########################
    # test()

