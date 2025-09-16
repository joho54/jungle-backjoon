# label: 누적합(슬라이딩 윈도우가 아님)

import sys

def solve(n: int, k: int, arr: tuple):
    # prefix sum 초기화
    pref = [0] * (n+1)
    for i in range(n):
        pref[i+1] = arr[i] + pref[i]
    
    ans = -sys.maxsize
    for i in range(k, n+1):
        tmp = pref[i] - pref[i-k] # 
        ans = max(tmp, ans)
    return ans
    

if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    arr = tuple(map(int, input().split()))
    print(solve(n, k, arr))