# label: 투 포인터
# 윈도우 최소 갱신하면서 윈도우를 1씩 증가시키면 됨. 최소값은 계속 최대힙에 추가.

import sys
from collections import deque

def solve(n: int, k: int, arr: tuple):
    result = []
    dq = deque()
    for i in range(n):
        # 범위 제거
        while dq and dq[0] < i - k + 1: 
            dq.popleft()
        # arr보다 큰 값 제거
        while dq and arr[dq[-1]] > arr[i]:
            dq.pop()
        # 현재 값을 데크에 추가
        dq.append(i)
        # 만약 인덱스가 오른쪽 윈도우 경계보다 크다면
        if i > k - 1:
            result.append(arr[dq[0]])
    return max(result)
        
if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    arr = tuple(map(int, input().split()))
    print(solve(n, k, arr))