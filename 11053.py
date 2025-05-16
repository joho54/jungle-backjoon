"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

import sys

def recur(n, arr):
    dp = [1 for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
        ans = max(ans, dp[i])
    return ans

def test():
    n = 6
    arr = (10, 20, 10, 30, 20, 50)
    assert recur(n, arr) == 4
    n = 1
    arr = (10)
    assert recur(n, arr) == 1
    n = 2
    arr = (10, 20)
    assert recur(n, arr) == 2
    n = 2
    arr = (20, 10)
    assert recur(n, arr) == 1
    # 마지막 디피가 최대가 아닌 경우
    n = 6
    arr = (10, 20, 10, 30, 50, 10)
    assert recur(n, arr) == 3, f"마지막 요소가 앞보다 작을 때 문제 발생"

def submit(recur):
    input = sys.stdin.readline
    n = int(input().strip())
    arr = tuple(map(int, input().split()))
    print(recur(n, arr))

if __name__ == '__main__':	
    # submit(recur)
    test()

