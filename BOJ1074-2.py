# 자 수도코드를 그럼 다시 칠까? 그냥 해.

import sys

def recur(n, i, j, cnt): # i 번째에 왔을 때 그 뭐냐 음. 
    global r, c
    offset_size = 2**(n-1) # 사각형의 사이즈 설정
    
    # if base condition
    # 현재 인덱스 정보는 i, j에 담겨 있음.
    if i  == r or i == r - 1:  
        if (i, j) == (r, c): return
        j += 1
        cnt += 1
        if (i, j) == (r, c): return
        i += 1
        j -= 1
        cnt += 1
        if (i, j) == (r, c): return
        j += 1
        cnt += 1
        if (i, j) == (r, c): return
    # 대충 조건은 이런 느낌일 거 같아.
    # 그럼 인덱스는 어떻게 가야 해? 인덱스가 갈 필요가 있나? 그냥 뻔하지 않나?  이 값이 계속 커지다가. 어차피 말야.
    recur(n-1, i, j, cnt + offset_size)

n, r, c = list(sys.stdin.readline().split()) # suppose n = 4
recur(n, 0, 0, 0)