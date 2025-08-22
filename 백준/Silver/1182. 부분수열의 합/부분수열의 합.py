import sys

ans = 0
n, s = 0, 0

def solve(total: int, depth: int, arr: list, is_check: bool):
    global ans, n, s
    if total == s and is_check:
        ans += 1
    if depth == n:
        return
    
    solve(total, depth+1, arr, False)
    solve(total + arr[depth], depth+1, arr, True)
    
    

if __name__ == '__main__':
    input = sys.stdin.readline
    
    n, s = tuple(map(int, input().split()))
    arr = tuple(map(int, input().split()))
    solve(0, 0, arr, False)
    print(ans)
