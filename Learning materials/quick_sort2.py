def paritioning(A: list, left, right):
    if left >= right:
        return
    # A를 피벗을 기준으로 '피벗보다 작은 영역'과 '큰 영역'으로 나누는 함수
    # 파티션 배열의 양 끝에 포인터를 잡아줍니다.
    pl, pr = left, right
    # 피벗을 구해줍니다.
    p = A[(left+right)//2]
    # 두 포인터가 겹치지 않는 동안 포인터를 가운데로 스캔합니다.
    while pl <= pr:
        while A[pl] < p and pl < right: # 파티션을 벗어나지 않게 조건을 추가합니다!
            pl += 1
        while A[pr] > p and pr > left: # 이하 동일
            pr -= 1
        # 만약에 포인터가 멈췄고, 포인터 위치가 엇갈리지 않았다면 교환
        if pl <= pr:
            print(f'before: {A}')
            print(f'pivot: {p}, exchange: {A[pl]}, {A[pr]}')
            A[pl], A[pr] = A[pr], A[pl]
            pl += 1
            pr -= 1
            print(f'after: {A}')
    paritioning(A, left, pr) # 파티셔닝이 끝난 후 pr은 작은 그룹의 끝단에 위치하게 됨
    paritioning(A, pl, right)
    # 작업이 끝났다면 결과를 출력해줍니다.s

def quick_sort(A: list):
    paritioning(A, 0, len(A) - 1) # 배열 전체를 범위로 하는 파티셔닝 호출

A = [5, 4, 3, 2, 1, 4, 3, 6, 4]
quick_sort(A)
print(A)

