"""
1. 문제 읽기
이해 자체는 어렵지 않음.
2. 문제 풀기
분할정복의 방법론을 유도할 것. 
Phase1. 유도(유사한 문제 떠올려보기)
- 색종이? Z문제?: 2^n 길이의 정사각형을 다루는 문제들과는, 직사각형을 다룬다는 점에서 좀 다름
주어지는 데이터도 선형. n의 범위가 100,000으로 많지는 않은데, 주어지는 정수가 위 문제보다 큼
- 병합 정렬: 사실 근본적으로 비슷하겠지? 어떻게 비슷하려나. 
base case: 사각형을 나누다가 두 개가 남아서, 상수 시간 안에 문제 해결이 가능한 시점
recursion case: 주어진 히스토그램 부분에 대해 양쪽 히스토그램에서 구할 수 있는 최대 사각형
이건 당연히, 양쪽의 사각형 크기를 비교했을 때 최소 사각형 값을 리턴해야 한다. 
종이에 먼저 풀어보시길. 내가 봤을 땐 병합정렬하고 되게 비슷함
Phase2. 문제 정의
- 기본 문제: 전체 히스토그램에서 제일 큰 직사각형 찾기
- 부문제: 부분 히스토그램에서 제일 큰 직사각형 찾기
- 베이스 케이스: 두 히스토그램에서 제일 큰 직사각형 찾기: 무조건 두 직사각형을 합칠 필요는 없음!
Phase3. 어디서 막혔는가? 
분할 정복에서 정복, 병합 단계를 어떻게 해야할지 모르겠음.
병합 단계에서 좌 중 우 삼각형중 최대를 리턴하기d만 하면 된다고 함. 제발 재귀 요정을 믿어!

3. 수도 코드
4. 코드 구현
"""

import sys

input = sys.stdin.readline

def recur(arr: list, left: int, right: int):
    """좌중우 영역 중 최대 삼각형을 리턴"""
    # base case: 히스토그램 영역이 2 이하여서 상수시간 안에 판단 가능.
    # conquer
    if right - left == 0: #영역이 하나.
        return arr[right]
    # recursion case
    mid = (left+right)//2
    # divide
    left_rect = recur(arr, left, mid)
    right_rect = recur(arr, mid+1, right)
    # combine.
    # mid left 영역 탐색
    # 근데 여기 로직이 좀 다른 거 같은데. 양옆으로 변을 늘리는 경우와 안 늘리는 경우의 탐색을 해야 하는데?
    lo, hi = mid, mid + 1
    height = min(arr[lo], arr[hi])
    cross_area = height*2
    while lo > left or hi < right:
        if hi < right and (lo == left or arr[lo-1] < arr[hi+1]):
            hi += 1
            height = min(arr[hi], height)
        else:
            lo -= 1
            height = min(arr[lo], height)
        cross_area = max(cross_area, height * (hi-lo+1))
    
    return max(left_rect, cross_area, right_rect)

arr = []

while True:
    arr = tuple(map(int, input().split()))
    if arr == (0,): 
        break
    
    print(recur(arr[1:], 0, len(arr)-2))


"""
이슈: 시간초과

Phase1.
환경: 파이썬
로그: 8프로 맞춘 거 봐서 로직적인 에러는 없는거 같고, 복잡도 분석이 필요함.
최근 변경 사항: 재귀 함수로 구현

Phase2.
확인: 복잡도 분석: 딱 봐도 combine 과정에서 복잡함. 최악의 경우 O(n)임.
그러면 마스터 정리는 다음과 같음(O(n)을 n으로 생각하고)
T(n) = 2T(n/2) + n + c
    = ...
    = n^2 + n(2c-1)
O(n^2)(맞나?)
아무튼 컴바인 과정에서 복잡도 줄일 필요가 있음. 지금 선형탐색을 하는데, 메모이제이션을 해야 하나? 
시도: 피드백 다시 보니까 그게 문제가 아니라, 컴바인 로직이 다름. 근데 왜 다른지 모르겠음.
분석: 
"""