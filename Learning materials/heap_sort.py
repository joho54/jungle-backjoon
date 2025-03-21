# ### Phase3. 이제 좀 이해가 되시면 구현을 해 봅시다.

# 최소 요구사항 정리

# 1. 다운 힙을 구현하니다.
# 2. 다운힙 함수를 범위를 줄여가며 호출합니다.

from typing import MutableSequence

def heap_sort(A):
    def down_heap(A: MutableSequence, left, right):
        print(f'down heap called: {A[left:right+1]}')
        root = A[left]
        while left * 2 + 1 < right: # while root has child
            # 힙 성질을 구현
            lchild = left * 2 + 1 
            rchild = lchild + 1
            print(f'heap down. root: {root}, left: {A[lchild]}, right: {A[rchild]}')
            gt_child = lchild if A[lchild] > A[rchild] else rchild #큰아들 구하기
            print(f'compared {A[lchild]} v {A[rchild]}, choose {A[gt_child]}')
            if root >= A[gt_child]:
                print(f'root is already greatest value. root: {root}, gt-child:{A[gt_child]}')
                break
            print(f'exchanging family: {A[left], A[lchild], A[rchild]}')
            # 교환?
            A[left], A[gt_child] = A[gt_child], A[left]
            print(f'exchanged gt-child with parent: {A[:right+1]}')
            # 아래 요소에 대해 다운힙. 근데 이제 변경된 자식에 대해서만
            left = gt_child
            root = A[gt_child]
            print(f'next child: {A[left]}, index: {left}')
        

    # 이제? 아래서부터 다운힙 하면 됨
    n = len(A)-1
    print(f'sort start: {A}')
    for i in range(n//2-1, -1, -1): # 이때 올라가는 범위가 이런 느낌이었는데. 아 이거였나.
        down_heap(A, i, n) 
    # print(f'\ninitial down heap complete: {A}\n')
        # 힙으로 초기화
    # 이제 루트 하나씩 빼서 저장하고 전체에 대해 다운힙 진행.
    # 이때 해야 되는게 그... 루트 빼서 저장하고 다운힙하기 인데,
    # 첫 반복문은 뭘 해야되냐? 범위를 줄여가면서 다운힙을 실시해야지. right가 줄어듦.
    # complete = []
    for i in range(n, -1, -1):
        # 루트를 빼서 완성 정렬에 추가해주고
        # complete.append(A[0])
        # print(f'complete: {complete}')
        # 끝 값을 복사해서 올려준다.
        print(f'before exchange: {A}')
        A[i], A[0] = A[0], A[i]
        print(f'exchanging: {A[0]} <-> {A[i]} ')
        print(f'after exchange: {A}')

        print(f'\ni: {i}====================\n')
        # print(f'down heap complete: {A}\n')
        down_heap(A, 0, i-1)
    return A
    # return complete


print(heap_sort([4, 3, 4, 2, 4, 5, 2, 234, 3245, 5234, 4325, 3]))
        