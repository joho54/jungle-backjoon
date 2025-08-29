import sys

def solve(n, s, e):
    if {s, e} == {1, n}:
        print(0)
    elif s in (1, n) or abs(s-e) == 1:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n, s, e = tuple(map(int, input().split()))
        solve(n, s, e)
    
"""
0  
1 (0 0 e 0 0 s) (s 0 0 e 0 0) (0 0 s e 0 0)
2 (0 0 s 0 0 e) ()  

5 5 1
3 1 2
7 3 5
"""