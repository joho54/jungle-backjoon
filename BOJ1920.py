"""
보류
사유: 이분탐색을 모르면 제대로 풀 수 없음

import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
search_list = list(map(int, sys.stdin.readline().split()))
for val in search_list:
    if val in arr: print(1)
    else: print(0)

이건 내 지식으로 푼 오답 코드.

"""

"""
1. 문제 읽기: 어..이거 그냥 입력받고 in 연산자 쓰면 안 되나? 안 됨. 정렬한 다음 이진탐색해야 할듯
2. 문제 풀기: 
3. 수도 코드:
4. 코드 구현: 
"""

# def bin_search(A: list, val: int):
    
#     left = 0
#     right = len(A) - 1
#     while left <= right: # 파티션이 유효한 동안. 
#         center = (left+right)//2
#         idx = center # 영역의 절반을 인덱스로 고정
#         if A[idx] > val: # 답이 왼쪽 영역에 있음.
#             right = center # right idx를 반으로 감소
#         elif A[idx] < val: # 답이 오른쪽 영역에 있음.
#             left = center+1 # left를 높여서 영역을 반 좁히기
#         elif A[idx] == val: 
#             return 1
#     return 0

import sys

dictionary = {}


n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
for a in arr:
    dictionary[a] = True
m = int(sys.stdin.readline().strip())
search_list = list(map(int, sys.stdin.readline().split()))

for key in search_list:
    if dictionary.get(key, False): print(1)
    else: print(0)

"""
이슈: 무한 루프
Phase1.
환경: 파이썬
로그: 없음
최근 변경 사항: bin_search 이진 탐색 함수 작성
Phase2.
확인: 루프에 중단점 ㄱㄱ
배열 안에 값이 없을 경우 무한 루프를 돈다. 인덱싱을 하다가 
자연스럽게 파티션이 엇갈리면 끝나야 하는데, 파티셔닝 인덱스에 문제가 있다.
left, right 인덱스가 3, 4일때 무한 반복 발생.
center = 3(3.5)
left가 계속 3으로 업데이트 됨. 와 이거 어떻게 파티셔닝 해야 해결할 수 있지? 
작아지는 경우는 문제가 없는데, 중간값을 기준으로 크고, 배열에 없는 값을 구할 때 
left right 인덱스가 좁혀지지 않는다. 
인덱스를 잡을 때 '다음 왼쪽 영역을 left, center로 잡고, 
다음 오른쪽 영역을 center+1, right로 잡으니 해결
시도: 
    while left <= right: # 파티션이 유효한 동안. 
        ...
        elif A[idx] < val: # 답이 오른쪽 영역에 있음.
            left = center+1 # left를 높여서 영역을 반 좁히기

결과 분석: 정렬은 성공. 그런데 시간초과 발생. 정렬을 최적화해야 한다. 우선순위 큐를 써야 하나? 
한 라인에 입력돼서, 이게 sort 함수 쓰는게 제일 빠를텐데. 

이슈: 시간 초과 문제
Phase1
환경: 파이썬
로그: 시간 초과
최근 변경 사항: bin_search 로직 픽스 
Phase2.
확인:
정수의 범위는 엄청 넓다. 주어지는 자연수 리스트도 십만이다. 
현재 시간 복잡도: 정렬에 nlogn
탐색 시간 복잡도: logn
O(nlogn) + O(logn)
이걸 어떻게 개선하지? 입력에 필요한 오버헤드를 개선해야 하나? 근데 그런식의 문제는 아닐 거 같음.
시도: 맵을 써봐야 하나? 하긴 이 문제는 데이터의 수정/삭제가 필요 없다. 아 뭐야 그럼 맵이네!
분석: 성공!!


"""