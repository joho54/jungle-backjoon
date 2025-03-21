# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# 재귀 문제 푸는법
# 1. subproblem 정의
# 전혀 모르겠다. 
# n번째 퀸을 놓을 자리를 고민하고 있다. 지금은.
# 이미 해결했다. n-1개의 퀸을 놓는 문제는.
# n-1개의 퀸이 이미 놓여 있으므로 내가 할 일은 n번째 퀸을 놓을 수 있는 빈 자리를 고민하는 것이다.
# 빈자리에 전부다 놓을 수 있는가? 안 될 거 뭐 있나. 
# 

import sys

n = int(sys.stdin.readline().strip())

flag_a = [False for _ in range(n)]
flag_b = [False for _ in range(2 * n - 1)]
flag_c = [False for _ in range(2 * n - 1)]

Queens = [None for _ in range(n)]
cnt = 0

def recur(i):
    global cnt
    for j in range(n):
        if (flag_a[j] == False
            and flag_b[i+j] == False
            and flag_c[n - 1 + i - j] == False
            ):
            Queens[i] = j
            if i == n-1:
                cnt += 1
                continue
            flag_a[j] = True
            flag_b[i+j] = True
            flag_c[n - 1 + i - j] = True
            recur(i + 1)
            flag_a[j] = False
            flag_b[i+j] = False
            flag_c[n - 1 + i - j] = False

recur(0)
print(cnt)