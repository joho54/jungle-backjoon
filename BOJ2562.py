# a = [1, 2, 3, 4]
# a.index(1)
arr = [
    int(input())
    for _ in range(9)
    ]

print(max(arr))
print(arr.index(max(arr))+1)
