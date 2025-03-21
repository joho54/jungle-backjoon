"""
1. 문제 읽기: 이게 어떻게 이분 탐색이지? 
2. 문제 풀기
2-1. 아이디어 브레인 스토밍
가. prefix sum을 쓰기: 
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

print(h_x)

위 코드에 대한 분석: 문제에 대한 incremental method다. 이걸 divide and conquer 
방식으로 바꿔야 문제를 해결할 수 있을 것.
여기서 incremental한 요소는 

다. 

3. 수도 코드

"""

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

print(h_x)
"""
이슈: 
"""