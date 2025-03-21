# Phase1. 문제 읽기: 크기가 양수인 부분수열: 크기가 음수일 순 없으니, 0인 부분수열 제외하라는 말인듯
# Phase2. 손으로 풀기: 
# 5, 0 / -7 -3 -2 5 8
# Phase3. 수도 코드
# n 값이 최대 20으로, n^2 알고리즘으로도 충분함. 재귀로 모든 합을 구해서 맞으면 카운터 증가시키기?
# 베이스 컨디션: 모든 요소를 더했거나, 합의 값이 s와 같아졌거나
# 반복하면서 재귀, 플래그 관리
# Phase4. 코드 구현

n, s = tuple(map(int, input().split()))
arr = tuple(map(int, input().split()))

# n, s = 5, -100000 
# arr = [-7, -3, -2, 5, -100000]

flag = [False] * n
cnt = 0

def recur(A: int, start):
    global cnt
    if A == s and (True in flag):
        cnt += 1
    elif not (False in flag):
        return
    
    for i in range(start, n):
        if not flag[i]:
            flag[i] = True
            recur(A + arr[i], i+1)
            flag[i] = False
        
        
recur(0, 0)
print(cnt)

"""
이슈
Phase1 
환경: 파이썬
로그: 
base condition hit. 0, [False, True, True, True, False]

-3 -2 5 
base condition hit. 0, [False, True, True, True, False]

-3 -2 5 
base condition hit. 0, [False, True, True, True, False]

-3 -2 5 
base condition hit. 0, [False, True, True, True, False]

-3 -2 5 
base condition hit. 0, [False, True, True, True, False]

-3 -2 5 
base condition hit. 0, [False, True, True, True, False]

-3 -2 5 
6
최근 변경 사항: 코드 구현
Phase2
확인: 같은 케이스가 자꾸 더해짐. 앞에서부터 차례로 해주면 안 되나? 
반복문 수행할 
시도: 재귀할 때 start 인덱스를 설정
결과분석: 반복해서 더해지는 문제 해결

이슈
Phase1.
환경: 파이썬
로그: 틀렸습니다
최근 변경 사항: start 인덱스 설정함.

Phase2-1
확인: 그냥 틀림 어디서 틀리는 거지? 이럴 때는 경계값 테스트 해야지
경계값: 1 <=n <= 20, -1000000 <= S <= 100000
반복문 수행할 때 
시도: 
입력이 다음과 같을 때 
n, s = 5, -100000 
arr = [-7, -3, -2, 5, -100000]
아 이거 맞는데 그럼
결과분석:
"""
