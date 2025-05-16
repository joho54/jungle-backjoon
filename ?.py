from collections import deque

def recur(n):
    s = deque()
    while True:
        if n > 0:
            s.append(n)
            n = n - 1
            continue
        else:
            if s:
                n = s.pop()
            else:
                break
        print(n)
        n = n - 2

def recur2(n):
    if n > 0:
        recur2(n-1)
        recur2(n-2)
        print(n)
recur2(4)
# recur(4)