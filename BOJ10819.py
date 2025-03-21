# 문제 읽기
# 문제 풀어보기
# 인덱스를 잘못 읽어서 문제를 완전히 잘못 풀었다. 아래는 다시 푼 풀이
# 20 1 15 8 4 10이 있을 때
# |20 - 1| = 19로 최대 절대값
# |1 - ?| 를 구할 때는? 
# |1 - 15| = 14로 최대 절대값
# |15 - 4| = 11로 최대 절대값
# |8 - 10 = 2로 옵션 없음 -> 이게 좀 문제가 될 거 같음.
# 19 + 14 + 11 + 2
# 이런 방식으로 풀면 정답을 구할 수 없음.
# 아니면 모든 숫자 배열의 경우를 구해서? 값을 구하는 방법도 있지. 
# 어이가 없네 진짜 그건가? n도 워낙 작아서
# 그냥 재귀로 해.

import sys
MAX_INT = sys.maxsize

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

max_val = -MAX_INT

def pick(A):
    global max_val
    if(len(A) == n): 
        B = [
            arr[a] for a in A
        ]
        val = calc(B)
        max_val = max(max_val, val)
        return
    for idx in range(n): 
        if idx not in A: # 
            pick([*A, idx])

def calc(A):
    tmp = 0
    for i in range(1, n):
        tmp += abs(A[i-1] - A[i]) # | A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
    return tmp

#A를 다시 정의: 인덱스

pick([])  
print(max_val)
