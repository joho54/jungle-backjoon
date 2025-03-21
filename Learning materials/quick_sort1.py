import sys
n = int(input())
arr = tuple(map(int, sys.stdin.readline().split()))

def quick_sort(A: list) -> list:
    # base condition 
    n = len(A)
    if n == 2:
        return [A[0], A[1]] if A[0] > A[1] else [A[1], A[0]]
    elif n <= 1:
        return A
    # get pivot
    pivot = A[n//2]
    smaller, equal, larger = [], [], []
    for a in A:
        if a < pivot:
            smaller.append(a)
        elif a == pivot:
            equal.append(a)
        elif a > pivot:
            larger.append(a)
    return [*quick_sort(smaller), *equal, *quick_sort(larger)]

print(quick_sort(arr))
