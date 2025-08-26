import sys, bisect

def solve(arr: list, queries: list):
    arr.sort()
    for q in queries:
        pos = bisect.bisect_left(arr, q)
        if pos == len(arr):
            print(-1)
        elif arr[pos] != q:
            print(-1)
        else: print(pos)
    

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    arr = [
        int(input().strip())
        for _ in range(n)   
    ]
    queries = [
        int(input().strip())
        for _ in range(m)
    ]
    solve(arr, queries)