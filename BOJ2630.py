"""
1. 문제 읽기
우아 쉽다
2. 문제 풀기
그냥 재귀 쓰면 됨.
3. 수도 코드
ㄱㄱ
4. 코드 구현
ㄱㄱ
"""
import sys

cnt = [0, 0]
cnt[1] = 0
cnt[0] = 0

def is_base(n, r, c):
    area_sum = 0
    for row in range(r, r+n):
        area_sum += sum(rect[row][c:c+n])
    # print(f'area_sum of {n, r, c}: {area_sum}')
    if area_sum == n**2 or area_sum == 0: return True

def recur(n: int, r: int, c: int):
    global rect
    if n == 1:
        cnt[rect[r][c]] += 1
        return
    if is_base(n, r, c): 
        cnt[rect[r][c]] += 1
        return
    # 좌상
    half = n // 2
    recur(half, r, c)
    # 우상
    recur(half, r, c+half)
    # 좌하
    recur(half, r+half, c)
    # 우하
    recur(half, r+half, c+half)


n = int(sys.stdin.readline().strip())
rect = [
    tuple(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

recur(n, 0, 0)

print(cnt[0])
print(cnt[1])

"""
이슈: 영역 계산이 잘못 되고 있음.
Phase1.
환경: 파이썬
로그: 오답 출력
최근 변경 사항: is_base, recur 함수 작성

Phase2.
확인: 로그 찍어 보기. area sum 계산할 때 반복문에서 잘못 더해지고 있었음(계속 초기화)
시도:
area_sum = 0
    for row in range(r, r+n):
        area_sum += sum(rect[row][c:c+n])
위와 같이 수정
결과: 성공.

"""