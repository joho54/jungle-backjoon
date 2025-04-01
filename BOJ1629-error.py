import sys
input = sys.stdin.readline
A, B, C = tuple(map(int, input().split()))

def power(a: int, b: int):
    if b == 1: return a%C
    temp = power(a, b//2)
    if b%2 == 0: 
        return (temp*temp)%C
    else:
        return (temp*temp*a)%C

print(power(A, B))