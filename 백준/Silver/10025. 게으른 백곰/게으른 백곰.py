import sys
MAX_X = 1_000_000

def solve(arr, k):
    pref = [0] * (MAX_X + 1)
    for i in range(MAX_X):
        pref[i+1] = arr[i] + pref[i]
    ans = -sys.maxsize
    
    for i in range(MAX_X+1):
        left = max(0, i-k)
        right = min(i+k+1, MAX_X) # DEBUG: i+k+1 이유
        pref_sum = pref[right] - pref[left]
        ans = max(pref_sum, ans)
    print(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    arr = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    arr2 = [0 for _ in range(MAX_X)]
    for g, i in arr:
        arr2[i] = g
    solve(arr2, k)