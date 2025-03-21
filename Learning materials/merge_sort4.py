from collections import deque

def merge_sort(A):
    stack = deque()
    stack.append((0, len(A)-1, False))
    buff = [0]*len(A)

    while stack:
        left, right, merged = stack.pop()

        if left >= right:
            continue

        center = (left + right)//2

        if not merged:
            # 병합을 위해 스택에 다시 저장
            stack.append((left, right, True))
            stack.append((left, center := (left+right)//2, False))
            stack.append((center+1, right, False))
        else:
            # 병합 시작
            mid = (left + right)//2
            i, j, k = left, mid+1, left

            while i <= mid and j <= right:
                if A[i] <= A[j]:
                    buff[k] = A[i]
                    i += 1
                else:
                    buff[k] = A[j]
                    j += 1
                k += 1

            while i <= mid:
                buff[k] = A[i]
                i += 1; k += 1

            while j <= right:
                buff[k] = A[j]
                j += 1; k += 1

            for idx in range(left, right+1):
                A[idx] = buff[idx]

arr = [4, 4, 2, 5, 4342, -324, 5324, 24, 234, 234, 123, 243, 2435, 132, 243, 435, 3452]
merge_sort(arr)
print(arr)