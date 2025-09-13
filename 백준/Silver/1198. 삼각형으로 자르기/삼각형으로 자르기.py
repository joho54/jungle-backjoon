import sys

ans = 0

def shoetie(triangle: list):
    p1, p2, p3 = triangle
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    breadth = 0.5 * abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)) 
    return breadth

def recur(triangle: list, idx: int, n: int, points: list):
    global ans
    if len(triangle) == 3:
        ans = max(ans, shoetie(triangle))
        return
    for i in range(idx, n):
        triangle.append(points[i])
        recur(triangle, i+1, n, points)
        triangle.pop()

def solve(n: int, points: list):
    global ans
    triangle = []
    recur(triangle, 0, n, points)
    return ans
    

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    points = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    
    print(solve(n, points))