import sys

def euclidiean(a: int, b: int):
    while b != 0:
        a, b = b, a%b
    return a

def solve(a: int, b: int, x: int):
    gcd = euclidiean(a, b)
    return x//gcd

if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        a, b, x = tuple(map(int, input().split()))
        print(solve(a, b, x))