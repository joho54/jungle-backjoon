# 1. 문제 읽기
# 2. 문제 풀기
# 3. 수도 코드
# 4. 코드 구현

def is_base(A: list, r: int, c: int, n: int):
    """A 배열의 r, c를 시작점으로 하는 n 영역의 합을 구하고, 0이거나 n^2이면 True를 리턴"""
    pixels = 0
    for i in range(r, r+n):
        for j in range(c, c+n):
            pixels += A[i][j]
    if pixels == 0: return 0
    elif pixels == n**2: return 1
    return -1

def recur(A: list, r, c, n):
    pixels = is_base(A, r, c, n)
    if pixels != -1:
        print(pixels, end='')
        return
    # 1 사분면 재귀
    half = n//2
    print('(', end='')
    recur(A, r, c, half)
    # 3 사분면 재귀
    recur(A, r, c+half, half)
    # 2 사분면 재귀
    recur(A, r+half, c, half)
    # 4 사분면 재귀
    recur(A, r+half, c+half, half)
    print(')', end='')
        

n = int(input())
arr = [
    tuple(map(int, list(input())))
    for _ in range(n)
]

recur(arr, 0, 0, n)
