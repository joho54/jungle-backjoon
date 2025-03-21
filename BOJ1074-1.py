import time

start_time = time.time()  # 시작 시간 기록

from collections import deque

s = deque()

class rect:
    def __init__(self, r1, c1, r2, c2):
        self.r1 = r1
        self.c1 = c1
        self.r2 = r2
        self.c2 = c2
    def __str__(self):
        return f'{self.r1, self.c1, self.r2, self.c2}'

def get_rect(pos, T: rect):
    half_r = (T.r1 + T.r2)//2
    half_c = (T.c1 + T.c2)//2
    if pos == 'A':
        return rect(T.r1, T.c1, half_r, half_c)
    if pos == 'B':
        return rect(T.r1, half_c, half_r, T.c2)
    if pos == 'C':
        return rect(half_r, T.c1, T.r2, half_c)
    if pos == 'D':
        return rect(half_r, half_c, T.r2, T.c2)
    

def recur(T: rect): # 사각형 하나가 주어졌을 때, T에 대한 A, B, C, D 사각형을 구해서 재귀
    global grid, cnt
    if abs(T.r1 - T.r2) == 2:
        for i in range(T.r1, T.r2):
            for j in range(T.c1, T.c2):
                # print(i, j)
                grid[i][j] = cnt
                cnt += 1
        return
    A = get_rect(pos='A', T=T)
    B = get_rect(pos='B', T=T)
    C = get_rect(pos='C', T=T)
    D = get_rect(pos='D', T=T)
    recur(A)
    recur(B)
    recur(C)
    recur(D)


def recur2(T: rect):
    global grid, cnt
    while True:
        if abs(T.r1 - T.r2) == 2:
            # 현재 업데이트된 사각형이 충분히 작다면 방문을 한 다음 종료.
            for i in range(T.r1, T.r2):
                for j in range(T.c1, T.c2):
                    grid[i][j] = cnt
                    cnt += 1
            T = s.popleft()
            continue
        if s: 
            s.appendleft(get_rect('D', T))
            s.appendleft(get_rect('C', T))
            s.appendleft(get_rect('B', T))
            s.appendleft(get_rect('A', T))
            T = s.popleft()
            continue
        break



# initial T must contain correct r, c ponits.
n, r, c = tuple(map(int, input().split()))
n = 2**n
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
cnt = 0
initial_rect = rect(0, 0, n, n)
recur(T=initial_rect)
print(grid[r][c])
# for g in grid:
#     print(g)

# 실행할 코드
sum_val = sum(range(10**6))

end_time = time.time()  # 종료 시간 기록

execution_time = end_time - start_time
print(f"실행 시간: {execution_time:.6f} 초")

start_time = time.time()  # 시작 시간 기록

grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
cnt = 0
initial_rect = rect(0, 0, n, n)
s.appendleft(initial_rect)
recur(T=initial_rect)
print(grid[r][c])


# 실행할 코드
sum_val = sum(range(10**6))

end_time = time.time()  # 종료 시간 기록

execution_time = end_time - start_time
print(f"실행 시간: {execution_time:.6f} 초")