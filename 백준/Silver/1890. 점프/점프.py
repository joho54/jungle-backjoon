import sys
from collections import deque

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n 

# def jump(n, grid):
#     table = [[0 for _ in range(n)]for _ in range(n)]
#     que = deque([(0, 0)])
#     table[0][0] = 1
#     while que:
#         r, c = que.popleft()
#         if (r, c) == (n-1, n-1): continue
#         x = grid[r][c]
#         if in_range(r+x, c, n):
#             table[r+x][c] += table[r][c]
#             que.append((r+x, c))
#         if in_range(r, c+x, n):
#             table[r][c+x] += table[r][c]
#             que.append((r, c+x))
#     return table[n-1][n-1]

def jump(n, grid):
    table = [[0 for _ in range(n)]for _ in range(n)]
    table[0][0] = 1
    for r in range(n):
        for c in range(n):
            if (r, c) == (n-1, n-1): continue
            x = grid[r][c]
            if in_range(r+x, c, n):
                table[r+x][c] += table[r][c]
            if in_range(r, c+x, n):
                table[r][c+x] += table[r][c]
    return table[n-1][n-1]

def submit(jump):
    input = sys.stdin.readline
    n = int(input().strip())
    grid = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    print(jump(n, grid))

def test():
    n = 4
    grid = [(2, 3, 3, 1),
            (1, 2, 1, 3),
            (1, 2, 3, 1),
            (3, 1, 1, 0)]
    assert jump(n, grid) == 3

if __name__ == '__main__':	
    submit(jump)
    # test()

