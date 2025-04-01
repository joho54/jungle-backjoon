"""
1. 문제 읽기
2. 문제 풀기
느낌상 수열의 길이를 x로 잡고 이진탐색 때리면 될 거 같기도 하고?
최대 길이가 x인 수열이 존재하는가? 
- 없으면 길이 x를 줄임
- 있으면 길이 x를 늘임
A에서 길이 x의 수열을 구하는 방법: 백트래킹 조합?
3. 수도 코드
4. 코드 구현
"""
import sys
n = int(sys.stdin.readline().strip())
arr =  list(map(int, sys.stdin.readline().split()))
max_len = 1

def get_list(current_array: list, goal_len: int, idx: int):
    global arr, max_len
    """
    배열 (global) arr에서 길이가 goal_len인 수열을 재귀적으로 구하는 함수
    idx: 현재까지 A에서 고려한 인덱스. 
    idx를 포함하는 경우를 넘기거나, 포함하지 않는 경우를 넘긴다.
    최종 목적: goal_len 길이의 부분수열을 전체 수열 arr에서 구할 수 있는가?
    """
    # base case
    if len(current_array) == goal_len:
        # print(f'base hit {current_array}') # 전역 max_len 업데이트
        max_len = max(goal_len, max_len)
        return 
    # 만약 인덱스가 끝났으면?
    if len(arr) == idx:
        return 
    # recursion case
    # print(f'getting in to recursion. ?? {current_array} <- {arr[idx]}')
    if len(current_array) == 0 or current_array[-1] < arr[idx]: # 현재 부분 수열의 마지막 값이 idx보다 작다면
        get_list([*current_array, arr[idx]], goal_len, idx+1)
        get_list(current_array, goal_len, idx+1)


def get_max_array(left: int, right: int):
    global max_len
    center = (left+right)//2
    while left < right: 
        current_max_len = max_len
        get_list([], center, 0) #이게 전역 변수 max_len을 업데이트
        # print(f'goal now {center}')
        if current_max_len != max_len:
            # 만약 center 길이의 부분 수열이 존재한다면!
            # 일단 저장! -> 이걸 전역에서 바로 구한다음 처리
            # max_len = max(max_len, center)
            # print('update!')
            # 그리고 존재한다고 하니, 이제 더 볼드한 트라이를 해 보는거지
            # print('try bold!!'*10)
            left = center + 1
        else: # center 길이의 부분 수열이 존재하지 않는다면!
            # 더 소심하게 시도
            # print('not found'*10)
            right = center
        
        center = (left+right)//2 # center 업데이트

get_max_array(0, 1000)
print(max_len)

"""
이슈: 틀렸습니다.
Phase1.
환경: 파이썬
로그: 틀렸습니다
최근 변경 사항: 이진 검색으로 답 구하는 함수 구현
Phase2.
확인: 문제 조건 확인
수열의 크기는 1 이상 1000 이하
수열로 올 수 있는 값은 1 이상 1000 이하
시도: 경계값
1. 수열의 크기가 1인 경우
2. 수열의 크기가 전부 같은 경우
3. 수열의 크기가 감수하는 경우
4. 수열의 크기가 감소하다가 증가하는 경우 <- 찾았다.
자세한 로그
5
5 4 3 4 5
getting in to recursion. ?? [] <- 5
getting in to recursion. ?? [5] <- 4
getting in to recursion. ?? [5] <- 3
getting in to recursion. ?? [5] <- 4
getting in to recursion. ?? [5] <- 5
getting in to recursion. ?? [] <- 5
getting in to recursion. ?? [5] <- 4
getting in to recursion. ?? [5] <- 3
그냥 같거나 크지만 않으면 재귀를 하면 됨! 혹은 none이거나. 
그럼 다음 질문! 재귀를 해서 값이 업데이트 되면 뭘 어떡하면 됨? 
재귀 스택 끝에 값을 리턴 시키는 방법을 모르니, 그냥 전역 변수를 플래그로 써야할 거 같음.
결과 분석:
"""