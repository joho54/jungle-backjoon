def partitioning(A: list, left, right):
    # 파티션 유효성 검사
    if left < right:
        partitioning(A, left, (left+right)//2)
        partitioning(A, (left+right)//2+1, right)
        # 인덱스 설정
        p = k = 0
        i = j = left
        center = (left+right)//2
        
        # 배열의 앞 부분을 버퍼에복사 
        while i <= center: 
            buff[p] = A[i] # p는 버퍼의 시작 지점(0), i는 파티션의 시작지점 = left
            p += 1
            i += 1
        
        # 버퍼와 파티션을 병합
        # k는 버퍼의 두 번째 포인터?
        # j는 배열의 정렬용 포인터
        while k < p and i <= right:
            if buff[k] < A[i]: # 버퍼에 있는 친구가 작으면
                A[j] = buff[k]
                k += 1 # 버퍼 포인터 늘리고
            else:
                A[j] = A[i]
                i += 1 # 배열의 뒷 부분 포인터 늘리고
            j += 1 # 정렬용 포인터 늘리고
        # 버퍼 떨이 처리
        while k < p:
            A[j] = buff[k]
            k += 1



A = [34, 4, 5, 2, 4, 6, 534, -123]
buff = [None for _ in range(len(A))]
partitioning(A, 0, len(A)-1)
print(A)