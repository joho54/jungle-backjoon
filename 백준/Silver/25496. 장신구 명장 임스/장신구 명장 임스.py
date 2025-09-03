import sys

def solve(p: int, n: int, a: list):
    a.sort()
    p = 200 - p
    idx = 0
    while p > 0:
        if idx >= n: break
        p -= a[idx]
        idx += 1
    print(idx)
        
        

if __name__ == '__main__':
    input = sys.stdin.readline
    p, n  = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    solve(p, n, a)