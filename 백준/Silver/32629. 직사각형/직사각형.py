import sys, math

def solve(n: int):
    ans = sys.maxsize
    for x in [max(1, int(math.sqrt(n))-2), int(math.sqrt(n)), int(math.sqrt(n))+2, n//2]:
        if x == 0: continue
        tmp = 2*x + 2 * math.ceil(n/x)
        ans = min(ans, tmp)
    return ans
        

if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(solve(n))
    