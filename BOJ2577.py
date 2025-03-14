a = int(input())
b = int(input())
c = int(input())

n = a * b * c
str_n = str(n)
ans = [0 for _ in range(10)]
for s in str_n:
    ans[int(s)] += 1
for a in ans:
    print(a)