from typing import MutableSequence

def m_sort(A: MutableSequence, left, right):
    if left >= right:
        return
    # pointer set
    idx_a = 0
    sort_ptr = 0
    buff_1 = 0
    buff_2 = 0
    center = (left+right)//2
    # initial recursion
    m_sort(A, left, center) 
    m_sort(A, center+1, right) # 뒷 파티션이 1 더 작음
    # merge
    ## buff에 저장
    while idx_a < center:
        buff[buff_1] = A[idx_a]
        idx_a += 1
        buff_1 += 1
    ## 병합
    while buff_2 < buff_1:
        if buff[buff_2] < A[idx_a]:
            A[sort_ptr] = buff[buff_2]
            buff_2 += 1
        else: 
            A[sort_ptr] = A[idx_a]
            idx_a += 1 
        sort_ptr += 1
    
    ## 떨이 처리: 사실 아직도 왜 A에 대해서는 떨이 처리를 안해도 되는지 모르겠다.
    while buff_2 < buff_1:
        A[idx_a] = buff[buff_2]
        buff_2 += 1
        idx_a += 1


def merge_sort(A: MutableSequence):
    m_sort(A, 0, len(A))
    
a = [234, 423, 465, 24, 5643]
buff = [None] * len(a)
merge_sort(a)
del buff
print(a)