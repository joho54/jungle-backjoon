from typing import MutableSequence

def down_heap(A: MutableSequence, left, right):
    """left~right 영역의 배열을 힙으로 만든다.(가장 큰 자식을 부모와 비교하여 교환)"""
    while left*2 < right: #왜 이게 그렇지? 
        # 루트를 정하고, 오른쪽, 왼쪽 자식 인덱스를 구한다
        root = A[left] 
        idx_lc = left * 2 + 1
        idx_rc = idx_lc + 1 
        print(f'family: {root, A[idx_lc], A[idx_rc] if idx_rc <= right else 0}')
        # 큰 자식을 구한다.
        idx_gc = idx_lc
        if idx_rc <= right and A[idx_lc] < A[idx_rc]:
            idx_gc = idx_rc
        # 이미 루트가 제일 크다면(혹은 그것 중 하나라면) 이 아래는 더 볼 필요 없음
        if root >= A[idx_gc]:
            break
        # 교환 실시
        A[left], A[idx_gc] = A[idx_gc], A[left]
        print(f'exchanged: {A[left], A[idx_gc]}')
        # 루트를 업데이트하고 재귀(tail recursion)
        left = idx_gc 
    print(f'down heap complete: {A}')

def heap_sort(A: MutableSequence):
    # 최초 다운 힙 실시
    n = len(A)
    for i in range(n//2-1, -1, -1): # 리프 노드의 개수가 나머지의 절반+1이다!!
        down_heap(A, i, n-1)
    # 맨 앞에 힙을 뒤로 보내주고. 
    print(A)
    # right를 좁혀 가며 다운 힙과 교환을 반복
    for right in range(n-1, 0, -1):
        A[0], A[right] = A[right], A[0]
        print(f'exchanged max root: {A}, right: {right}')
        down_heap(A, 0, right-1)
    
    print(A)

arr = [5, 2, 5, 7, 5, 6, 8,10, 4, -243]
heap_sort(arr)
