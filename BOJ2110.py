"""
1. 문제 읽기:
2. 문제 풀기
2-1. recursive method. 거리 배열을 써야할 거 같은데.
import sys
sys.setrecursionlimit(10**8) # 10^8 까지 늘림.

n, c = tuple(map(int, sys.stdin.readline().split()))

X = [
    int(sys.stdin.readline().strip())
    for _ in range(n)
]

X.sort()

def get_min_distance(A:list):
    '''집에 배치하는 경우 거리의 최소값 구하기'''
    if len(A) >= 2:
        min_dist = sys.maxsize
        for i in range(1, len(A)):
            min_dist = min(min_dist, A[i]-A[i-1])
        return min_dist
    return 0

memo = {}
def set_router_recursively(A: list, X: list, idx_house: int, num_router: int):
    '''재귀적으로 X에서 라우터를 놓는 모든 경우를 A에 구합니다.'''
    '''바닥 조건: 마지막 집에 라우터 배치하는 경우에서 재귀했을 때, 라우터가 다 배치됐다면'''
    # 바닥 조건의 경우를 메모에 저장해놓고, 메모에 있는 경우 재귀 안 하면 안 되나.
    min_dist = get_min_distance(A)
    if memo.get(min_dist, False):
        return
    if idx_house == len(X)-1:
        if num_router <= 0:
            memo[min_dist] = True
        return
    # idx_house에 배치하는 경우
    set_router_recursively([*A, X[idx_house]], X, idx_house+1, num_router-1)
    # idx_house에 배치 안 하는 경우
    set_router_recursively(A, X, idx_house+1, num_router)

set_router_recursively([], X, 0, c)
print(max(memo.keys()))

1 2 4 8 9
그 서브 값도 오름차순이 아닐 것임 .
0 그다음 최적의 값을 모름

이진탐색을 활용한 백트래킹?

다음 체계는?

3. 수도 코드

4. 코드 구현

"""

""" 2트
1. 문제 읽기
2. 문제 풀기
최대 공유기 거리를 매개변수로 놓고 can_place함수를 통해 '이 거리로 할 수 있는지'판단 하는 과정을
이진탐색으로 진행.(문제 풀고 나면 나무 자르기 문제랑 어떻게 연관되는지 생각해보기)
3. 수도 코드
- 초기 입력을 받는다.
- left, right를 설정한다. 
- mid(공유기 최소 거리)를 가지고 can_place로 이터레이션하며 거리를 비교하여 불 자료형을 리턴
- 끝? 별거 없네.
4. 코드 구현
"""
import sys

n, c = tuple(map(int, sys.stdin.readline().split()))
MAX_H = 1_000_000_000
houses = [
    int(sys.stdin.readline().strip())
    for _ in range(n)
    ]

# 집을 정렬.

def can_place(min_dist: int, c_num):
    """min_dist로 집 사이에 공유기 c_num대를 놓을 수 있는지 판단한다."""
    # 선형 탐색해야지 뭐.
    count = 1
    c_idx = 0
    # print(f'inspecting {min_dist}')
    # print(f'{houses[c_idx]}', end=', ')
    for i in range(1, n):
        if houses[i] - houses[c_idx] >= min_dist:
            # print(f'{houses[i]} - {houses[c_idx]} >= {min_dist}')
            count += 1
            c_idx = i
            if count >= c_num: 
                # print(f'inspection proved success: {min_dist}')
                return True
    # print(f'inspection discovered as failure for {min_dist}') 
    return False


def solve():
    houses.sort()
    left, right = 0, MAX_H
    mid = (left + right) // 2
    max_mid = mid
    while left <= right:
        if can_place(mid, c):
            # print(f'can place at least {mid}')
            # try bolder
            left = mid + 1
            max_mid = mid # mid 저장.
        else:
            # try smaller
            right = mid - 1
        mid = (left + right) // 2
        # print(f'trying new area: {left} {mid} {right}')
    return max_mid
print(solve())

"""
이슈: 

Phase1.
환경: 파이썬
로그: 11프로만 정답. 
최근 변경 사항: can_place 와 solve 함수 작성

Phase2.
확인: 11프로 맞았으면 크게 틀린 건 아닐 수도 있는데. 또 반대로 틀린 테스트 케이스
찾기에 그렇게 어려운 것도 아니긴 하다.
근데 아무리 생각해도 can_place가 true일 때만 업데이트하는게 맞는데.
집 개수가 짝수일 때는 맞다.
홀수가 되면 1씩 작은 값을 내 놓는다. 왜 그렇지?
일단 짝수인 경우를 집중 공략.
세부 로그를 찍어본 결과 아래와 같은 결과.
inspecting 13
inspection discovered as failure for 13
inspecting 6
8 - 1 >= 6
inspection discovered as failure for 6
inspecting 2
4 - 1 >= 2
8 - 4 >= 2
inspection proved success: 2
can place at least 2
inspecting 4
8 - 1 >= 4
inspection discovered as failure for 4
2

2를 본 다음 4를 보고, 4를 실패한 다음 3을 안 보고 끝낸다.

시도: 
분석: 
"""
