a = int(input())
b = input()

anums, bnums = [0,0,0], [0,0,0]

for i in range(len(b)-1, -1, -1):
    print(a * int(b[i]))
print(a * int(b))