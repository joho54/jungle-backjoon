from typing import MutableSequence
from collections import deque

def partitioning(A: MutableSequence, left, right):
    s = deque()
    while True:
        
        pivot = A[(left+right)//2]
        pl, pr = left, right
        while pl <= pr:
            while pl < right and A[pl] < pivot:
                pl += 1
            while pr > left and A[pr] > pivot:
                pr -= 1

            if pl <= pr:
                A[pl], A[pr] = A[pr], A[pl]
                pl += 1
                pr -= 1


        # 여기가 뭐야? 작은 파티션 저장해놓고 큰 파티션 레지스트해서 보내버림.
        # 1. 둘 다 유효하다. 2. 하나만 유효하다. 3. 둘 다 안 유효하다.
        smaller = (left, pr)
        bigger = (pl, right)
        smaller_size = (pr-left) 
        bigger_size = (right-pl)
        
        if smaller_size > bigger_size: # switch.
            smaller, bigger = bigger, smaller
        
        if smaller[0] < smaller[1]: 
            s.append(smaller)
        if bigger[0] < bigger[1]: 
            left, right = bigger
            continue
        if s:
            left, right = s.pop()
            continue
        break

def quick_sort(A):
    partitioning(A, 0, len(A)-1)

a = [2345, 24352345, 23452345, 2346, 3, 1, 4,234, 2334, -234, 453, 342, 24543, 23452345, 43252345, 234553245]
quick_sort(a)
print(a)
