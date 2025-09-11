import sys

def solve(arr: list, window: int, n: int):
    pref = [0] * (n+1)
    for i in range(n):
        pref[i+1] = pref[i] + arr[i]
    ans = 0
    for i in range(n+1):
        left = max(0, i-window)
        right = i
        pref_sum = pref[right] - pref[left]
        if pref_sum >= 129 and pref_sum <= 138:
            ans += 1
    print(ans)
        

if __name__ == '__main__':
    input = sys.stdin.readline
    n, l = tuple(map(int, input().split()))
    arr = tuple(map(int, input().split()))
    solve(arr, l, n)