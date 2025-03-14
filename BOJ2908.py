def reverse_int(string: str):
    return int(string[::-1])

a, b = tuple(map(str, input().split()))
ra, rb = [reverse_int(elem) for elem in [a, b]]
print(max(ra, rb))