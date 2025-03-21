# 이거 디피로 은근 쉽게 풀 수 있었는데.
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 0.1 초 (하단 참고)	256 MB	50622	19238	14787	38.535%
# 문제
# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.


# 손으로 풀어보기.


import sys

# input
A = list(sys.stdin.readline().strip())
B = list(sys.stdin.readline().strip())

m, n = len(A), len(B)

dp = [[0 for _ in range(m)] for _ in range(n)]

# init dp
def init(A, B, m, n, dp):
    tmp = 0
    for i in range(m):
        if B[0] == A[i]: tmp = 1
        dp[0][i] = tmp

    tmp = 0
    for j in range(n):
        if A[0] == B[j]: tmp = 1
        dp[j][0] = tmp

init(A, B, m, n, dp)

string = ''
for i in range(1, m):
    for j in range(1, n):
        hit = dp[i-1][j-1] + 1 if A[i] == B[j] else 0
        # if hit != 0:
            # string += A[i] # 이 시점에서는 완성된 문자열을 알 방법이 없음. 완성된 테이블을 탐색해서 알아내야 함.
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], hit)

# ### Nested Phase 1. 구현 팁 확인

# **LCS 문자열 구하기 (Backtracking)**

# •	dp[m][n]부터 **거꾸로 탐색**하면서 문자열을 추출.

# •	A[i] == B[j]이면 **해당 문자는 LCS 문자열의 일부**이므로 저장.

# •	dp[i-1][j] > dp[i][j-1]이면 **위쪽으로 이동**, 아니면 **왼쪽으로 이동**.

# ### Nested Phase 2. 직접 구현하기.
