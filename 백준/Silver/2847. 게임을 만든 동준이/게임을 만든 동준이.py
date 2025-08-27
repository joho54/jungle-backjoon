'''
4
5
3
7
5
'''

import sys

def solve(n: int, arr: list):
    ans = 0
    for i in range(n-2, -1, -1):
        if arr[i] >= arr[i+1]: # 앞에 있는 애가 더 크다면
            sub = arr[i] - arr[i+1] + 1 # 5 7 -> 3
            arr[i] -= sub
            ans += sub
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    arr = [
        int(input().strip())
        for _ in range(n)
    ]
    print(solve(n, arr))