from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:
    """병합 정렬"""

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 재귀적으로 병합정렬"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center) # 배열 앞부분을 병합 정렬
            _merge_sort(a, center + 1, right) # 배열 뒷부분을 병합정렬
            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p:
                if buff[i] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1
    n = len(a)
    buff = [None] * n # 작업용 배열을 생성
    _merge_sort(a, 0, n - 1) # 배열 전체를 병합 정렬.
    del buff