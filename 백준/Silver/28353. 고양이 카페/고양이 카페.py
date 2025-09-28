import sys

def solve(n: int, k: int, arr: list):
    left = 0
    right = n-1
    cnt = 0
    arr.sort()
    while left < right:
        while arr[left] + arr[right] > k and left < right:
            right -= 1
        if left >= right:
            break
        # right 인덱스는 충분히 작아진 상황. (아래 조건은 불필요)
        # if arr[left] + arr[right] <= k:
        cnt += 1
        left += 1
        right -= 1
    return cnt
            
            

if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(solve(n, k, arr))