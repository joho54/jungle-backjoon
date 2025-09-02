import sys, math

def solve(a, b, h):
    x = (a*h)/(b-a)
    r1_sqr = x**2 + a**2
    r2_sqr = (x+h)**2 + b**2
    return math.pi * (r2_sqr - r1_sqr)

if __name__ == '__main__':
    input = sys.stdin.readline
    a, b, h = tuple(map(int, input().split()))
    print(solve(a, b, h))