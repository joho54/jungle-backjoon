# ### Phase1. 병합정렬 요구사항 정리

# 1. 파티션이 유효한 동안 루프
# 2. 앞 부분, 뒷 부분 재귀
# 3. 포인터 적절히 초기화
# 4. 버퍼에 앞 부분 복사
# 5. 버퍼와 뒷 부분 병합
# 6. 버퍼 떨이 처리.

# center 인덱스에 유의할 것

from collections import deque

def merge_sort(A: list, left, right):
    s = deque()
    s.append((left,right))
    while True:
        if left < right:
            center = (left+right)//2
            # merge_sort(A, left, center) # 이 코드가 먼저 실행돼야 하긴 함.
            s.append((center+1, right)) # 두 번째 파티션을 집어넣고 후반의 코드를 실행
            # 바닥 조건을 쳤다면 저장해 둔 거 꺼내서 다람쥐가 도토리 까먹듯 하면 됨
            left = left
            right = center
        elif s:
            # merge_sort(A, center+1, right)
            left, right = s.pop()
            # 이때 유효성 검사 해야지 않나
            # continue를 넣으면 안 된다: 원래 코드가 매개변수를 업데이트하고 처음으로 가는게 아니라서.
        # set pointers
        center = (left+right)//2
        sorting_idx = left
        a_pointer = left
        b_pointer1 = 0
        b_pointer2 = 0

        # copy to buffer
        while a_pointer <= center:
            buff[b_pointer1] = A[a_pointer]
            b_pointer1 += 1
            a_pointer += 1
        

        print(f'merging {A[left:center+1]} {A[center+1:right+1]}')
        # merge two array A
        while b_pointer2 < b_pointer1 and a_pointer <= right:
            # compare
            if buff[b_pointer2] < A[a_pointer]:
                A[sorting_idx] = buff[b_pointer2]
                b_pointer2 += 1
            else:
                A[sorting_idx] = A[a_pointer]
                a_pointer += 1
            sorting_idx += 1
        print(f'merge complete {A[left:right+1]}')

        # 떨이 처리
        while b_pointer2 < b_pointer1:
            A[sorting_idx] = buff[b_pointer2]
            sorting_idx += 1
            b_pointer2 += 1 

        if not s:
            break



arr = [4, 4, 2, 5, 4342, -324, 5324, 24, 234, 234, 2435, 123,243, 3452, 435, 132, 243]
buff = [None for _ in range(len(arr))]

merge_sort(arr, 0, len(arr)-1)
print(arr)