# label: 시뮬레이션

import sys

def print_seq(arr: list, l: int, r: int):
    cnt = 1
    for i in range(l, r): # i+1과 비교
        if arr[i] != arr[i+1]: 
            cnt += 1
    return cnt
        
def modify_seq(arr: list, l: int, r: int):
    for i in range(l, r+1):
        if arr[i] == 'Z': arr[i] = 'A'
        else: arr[i] = chr(ord(arr[i])+1)
        

def solve(arr: list, queries: list):
    for query in queries:
        s, l, r = query
        l -= 1
        r -= 1
        if s == 1: # 1은 뭔데? 범위의 문자집합 출력
            print(print_seq(arr, l, r) )
        elif s == 2:
            modify_seq(arr, l, r)

if __name__ == '__main__':
    input = sys.stdin.readline
    n, q = tuple(map(int, input().split()))
    arr = list(input().strip())
    queries = [
        tuple(map(int, input().split()))
        for _ in range(q)
    ]
    solve(arr, queries)