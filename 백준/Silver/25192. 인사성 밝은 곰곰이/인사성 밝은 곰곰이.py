# label: Data Structure(set)

import sys

def solve(log: list):
    s = set()
    ans = 0
    for elem in log:
        if elem == 'ENTER':
            ans += len(s)
            s.clear()
        else:
            s.add(elem)
    ans += len(s)
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    log = [
        input().strip()
        for _ in range(n)
    ]
    print(solve(log))