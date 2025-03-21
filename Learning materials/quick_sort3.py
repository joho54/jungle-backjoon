from collections import deque

def partitioning(A: list, left, right):
    s = deque()
    while True:
        # if left >= right: # 만약 봐야 하는 파티션이 유효하지 않은 값(파티셔닝 할요소가 하나거나 없다면)이라면 패스
        #     return
        pivot = A[(left+right)//2]
        pl, pr = left, right
        while pl <= pr: # 파티션이 엇갈리지 않는 동안
            while A[pl] < pivot and pl < right: # 첫 번째 조건: 파티셔닝의 기본 원리. # 두 번째 조건: 영역 유지
                pl += 1
            while A[pr] > pivot and pr > left: 
                pr -= 1
            if pl <= pr: # 포인터 값이 유효하다면
                A[pl], A[pr] = A[pr], A[pl]
                pl += 1
                pr -= 1
        
        if left < right:
            # partitioning(A, left, pr)
            s.append((left, pr )) # 저장해주고
            left, right = pl,right
            continue
        if s:
            # partitioning(A, pl, right)
            left, right = s.pop()
            # left = pl
            # right = right
            continue
        break

def quick_sort(A):
    partitioning(A, 0, len(A)-1)
        
A = [4, 2, 5, 3, 243, 5534, 21, 3]
quick_sort(A)
print(A)