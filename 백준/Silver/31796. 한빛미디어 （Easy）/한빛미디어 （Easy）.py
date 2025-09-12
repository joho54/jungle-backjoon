# 라벨: 뭐지? 쉬워서 알긴 하겠는데 라벨은 모르겠음. 그냥 incremental 하게 풀면 됨

import sys

def solve(n: int, arr: list):
    arr.sort()
    current_min = arr[0]
    cnt = 1
    for i in range(1, n):
        if current_min * 2 <= arr[i]:
            current_min = arr[i]
            cnt += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    arr = list(map(int, input().split()))
    print(solve(n, arr))