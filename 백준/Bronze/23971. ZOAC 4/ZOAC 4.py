
import sys

def solve(h, w, n, m):
    vert = h//(n+1) + 1 if h % (n+1) != 0 else h//(n+1)
    hor = w//(m+1) + 1 if w % (m+1) != 0 else w//(m+1)
    return vert * hor

def submit(solve):
    input = sys.stdin.readline
    h, w, n, m = tuple(map(int, input().split()))
    print(solve(h, w, n, m))

def test():
    h, w, n, m = 5, 4, 1, 1
    assert solve(h, w, n, m) == 6

if __name__ == '__main__':
    submit(solve)
    # test()
