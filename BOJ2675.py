c = int(input())
for _ in range(c):
    r, s = tuple(map(str, input().split()))
    p = [
        elem * int(r) 
        for elem in s
    ]
    print(''.join(p))