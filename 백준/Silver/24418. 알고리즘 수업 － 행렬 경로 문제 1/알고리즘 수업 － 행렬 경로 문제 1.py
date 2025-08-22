import sys, math
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    matrix = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    
    ans1 = math.comb(2 * n, n)

    ans2 = n*n
    
    print(ans1, ans2)