n, x = tuple(map(int, input().split()))
grid = tuple(map(int, input().split()))

for elem in grid:
    if elem < x:
        print(elem, end=' ')