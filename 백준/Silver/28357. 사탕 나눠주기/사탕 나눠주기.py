

import sys

def get_candies(pivot: int, arr: tuple):
    result = 0
    for elem in arr:
        if elem > pivot:
            result += elem - pivot
    return result

def solve(n: int, k: int, arr: tuple):
    left, right = 0, max(arr)
    ans = sys.maxsize
    while left <= right:    
        pivot = (left + right) // 2
        required_candies = get_candies(pivot, arr)
        # 필요한 사탕이 k개보다 많음. 피벗을 늘려서 사탕을 줄여야 함
        if required_candies > k:
            left = pivot+1
            continue
        # 필요한 사탕이 k개보다 적음. 피벗을 줄여서 사탕 개수를 늘려야 함
        # 그 전에 저장을 해둬야 함.
        elif required_candies < k:
            ans = min(pivot, ans)
            right = pivot-1
            continue
        # 필요한 사탕이 k개와 같음 -> pivot이 정답.
        else:
            ans = pivot
            break
            
    return ans
            
            
            

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    arr = tuple(map(int, input().split()))
    print(solve(n, k, arr))