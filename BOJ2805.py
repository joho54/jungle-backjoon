"""
1. 문제 읽기: 이게 어떻게 이분 탐색이지? 
2. 문제 풀기
2-1. 아이디어 브레인 스토밍
가. prefix sum을 쓰기: 말도 안 됨.
나. 완전탐색: 아래가 정답이다.
import sys

MAX_INT = sys.maxsize

n = 5
m = 20
trees = [4, 42, 40, 26, 46]

def cut_sum(height: int):
    sum_tmp = 0
    for tree in trees:
        sum_tmp += tree - height if tree > height else 0
    return sum_tmp

h_x = 0
prev_difference = MAX_INT

for i in range(0, max(trees)):
    cut_amount = cut_sum(i)
    difference = abs(cut_amount-m)
    if difference < prev_difference: # update
        prev_difference = difference
        h_x = i

# print(h_x)



다. 인크레멘탈 메서드에서 분할정복으로!

위 코드에 대한 분석: 문제에 대한 incremental method다. 이걸 divide and conquer 
방식으로 바꿔야 문제를 해결할 수 있을 것.
여기서 incremental한 요소는 i이다.

이제 이것을 정리해 보았을 때 cut_sum(i)-m이라는 우하향 함수가 있다. 
(i가 incremental 하다고 가정.)
그럼 다음과 같이 분기
cut_sum(i)-m > 0: 오른쪽 영역 디바이드
cut_sum(i)-m < 0: 왼쪽 영역으로 디바이드


3. 수도 코드

"""

import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
trees = tuple(map(int, sys.stdin.readline().split()))


def f(height: int):
    """
    f의 정의: height에 대해 나무를 잘랐을 때 얻게 되는 나무들의 길이에서 목표 길이를 뺀 것.
    """
    sum_tmp = 0
    for tree in trees:
        sum_tmp += tree - height if tree > height else 0
    return sum_tmp - m

def bin_search():
    """목표: f(h_x)를 최소화 하는 h_x 찾기"""
    left, right = 0, 1_000_000_001
    prev_center = None
    while left < right:
        # print(f'{left} --- {right}')
        i_center = (left+right)//2 # i for representing incremental parameter
        difference = f(i_center)
        # print(f'difference is {difference}.')
        if difference < 0: 
            # print(f'conquer left')
            left, right = left, i_center 
            if left >= right:  # 나무를 자르지 않는 높이에서, 다음 턴에 탐색을 마친다면!
                return prev_center # 아, 둘 다 그거일 수 있구나. 두 턴 다 음수가 나올 수도 있음.
        elif difference > 0: 
            # print(f'conquer right')
            left, right = i_center+1, right
            prev_center = i_center
            # 이때는 i_center가 무조건 나무를 잘라가는 것을 보장 여기서 갱신 필요
        else: # 차이가 0과 같음(best case)
            return i_center
    return i_center

ans = bin_search()

print(ans)
"""
이슈: 무한 루프

Phase1.
환경: 파이썬
로그: 무한 루프
최근 변경 사항: 이진 탐색 코드 작성

Phase2-1
확인: 로그를 어디 찍어야 하지? 
비교 로직이 좀 잘못 됐다. 
1. 구한 결과의 높이 차이를 구한다.
시도:
분할 정복 로직이 잘못돼 있었음. 함수의 우하향을 고려하지 않고, 잘못 작성.
그리고 절대값도 씌우면 안 됐음
if difference < 0: 
    # print(f'conquer left')
    left, right = left, i_center
elif difference > 0: 
    # print(f'conquer right')
    left, right = i_center + 1, right
else: # 차이가 0과 같음(best case)
    return i_center
결과 분석: 예제는 다 맞추지만 틀리는 테스트 케이스 존재.

이슈: 오답 발생
Phase1.
환경: 파이썬
로그: 틀렸습니다
최근 변경 사항: 이진 탐색 코드 로직 수정.

Phase2-1
확인: 이럴 땐 문제 조건을 타이핑하고, 경계값으로 테스트
1 <= N <= 1,000,000
1 <= M <= 2000000000 (잘라 가야 하는 나무 )
각 나무의 높이(i_center) 0 ~ 1,000,000,000 
각 나무의 높이가 0일수도 있다. 근데 나무 높이의 합은 항상 M보다 크다 했다.
M이 1 이상이니까 나무 높이의 합도 1 이상일 것.
찾았다.
2 1 <= 나무의 갯수 2, 잘라가야 하는 나무 값 1
2 2 <= 각 나무의 높이 2.
2 <= 설정한 커팅 높이: 2. 이러면 0에 수렴하긴 하겠지만, 문제의 조건과 다름. 
정답 커팅 높이: 1. 그러면 얼마를 자르지? 2를 자름. 
높이    자른 합    정답과 차이
2       0       1
1       2       1
0       4       3
i_center가 작을수록 나무가 커짐. 내 생각에는 인덱스 분할할 때 인덱스가
왼쪽 영역 / 오른쪽 영역 이렇게 잡히는게 좋은데?
적어도 M미터!!!!!!!!!!!!!!!!!!!!
마지막에 difference를 >= 0으로 만들때만 끝내야 한다!
안 자르는게 나은 경우가 생겨버리는데, 더 자르게 하는 방법은 없나? 이럴 땐 조건을 
찾아야 한다.

어쩄든 차이가 0보다 작을 때는 
일단 가져가긴 해야 함.
그러면.. 조건을 어떻게 잡지? 인덱스를... 1씩 바꿔 볼까
아 이거 어떡하지. 결과 값이 0일 수는 없는 건데. 만약 0일때는 i 값을 
시도: 
결과 분석
"""