"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

import sys

def make_lans(lans: list, cut_point: int) -> int:
    make_count = 0

    for len in lans:
        make_count += len//cut_point

    return make_count

def solve(n: int, lans: list):
    max_val = max(lans)
    min_val = 1
    result = 0
    max_mid = 0
    while(min_val <= max_val):
        mid = (min_val + max_val) // 2
        result = make_lans(lans, mid)
        if (result < n): # 개수가 부족함. min을 내려줘야 함.
            max_val = mid-1
        elif (result >= n):
            min_val = mid+1
            max_mid = max(max_mid, mid)
    return max_mid
    
if __name__ == '__main__':	
    input = sys.stdin.readline
    k, n = tuple(map(int, input().split()))
    lans = [0] * k
    for i in range(k):
        lans[i] = (int(input().strip()))
    print(solve(n, lans))