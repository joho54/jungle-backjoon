import sys

ans = sys.maxsize

def traverse(a: int, b: int, depth: int):
    global ans
    if a == b: 
        ans = min(ans, depth)
        return
    if a > b:
        return
    
    traverse(a*2, b, depth+1)
    traverse(int(str(a)+'1'), b, depth+1)

if __name__ == '__main__':
    input = sys.stdin.readline
    
    a, b = tuple(map(int, input().split()))
    
    traverse(a, b, 1)
    
    if ans == sys.maxsize:
        print(-1)
    else:
        print(ans)