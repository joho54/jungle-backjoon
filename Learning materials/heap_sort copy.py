from typing import MutableSequence

def heap_sort(a: MutableSequence):

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        temp = a[left]

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= right and a[cr] > a[cl] else cl # choose larger child
            if temp >= a[child]:
                break 
            a[parent] = a[child]
            parent = child
        a[parent] = temp
    
    n = len(a)

    for i in range((n - 1) // 2, -1, -1):
        down_heap(a, i, n - 1)

    for i in range((n-1) // 2, -1, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i - 1)

if __name__ == '__main__':
    num = int(input())
    x = [None] * num

    for i in range(num):
        x[i] = int(input())

    heap_sort(x)