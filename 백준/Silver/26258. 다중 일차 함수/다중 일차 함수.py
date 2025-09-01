import bisect, sys

class Wrapper:
    def __init__(self, value) -> None:
        self.value = value
    
    def __lt__(self, other):
        return self.value < other[0]

def solve(points: list, ks: list):
    
    for k in ks:
        pos = bisect.bisect_left(points, (k, 0))
        y1, y2 = points[pos-1][1], points[pos][1]
        if y2 - y1 < 0:
            print(-1)
        elif y2 - y1 > 0:
            print(1)
        else:
            print(0)
        

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    points = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    m = int(input().strip())
    ks = [
        float(input().strip())
        for _ in range(m)
    ]
    solve(points, ks)