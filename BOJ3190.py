"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

import sys
from collections import deque

snake = deque()
snake.append((0,0))

input = sys.stdin.readline

n = int(input().strip())
k = int(input().strip())
apples = [
    tuple(map(int, input().split()))
    for _ in range(k)
]
l = int(input().strip())
directions = [
    input().split()
    for _ in range(l)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def move(d: int) -> bool:
    """d 방향으로 1칸 이동시킨다."""
    global snake
    mapper = (
        (-1, 0), # U
        (0, 1), # R
        (1, 0), # D
        (0, -1) # L
    )
    new_head = (snake[0][0] + mapper[d][0], snake[0][1] + mapper[d][1])
    print(f'moving to {new_head}. current direction: {d}, full snake: {snake}')
    if not in_range(new_head[0], new_head[1]) or new_head in snake:
        print(f'hit!')
        return False
    if new_head not in apples: 
        print(f'snake pop. {new_head} is not in {apples}')
        snake.pop()
    else: print(f'ate apple!')
    snake.appendleft(new_head)
    return True

def simulate():
    cnt = 0
    d = 1
    i = 0
    while move(d):
        if i < len(directions) and cnt == int(directions[i][0]): # 방향 전환 타이밍
            print(f'changing direction')
            if directions[i][1] == 'L':
                d = (d+3)%4
            else:
                d = (d+1)%4
            i += 1
        cnt += 1
    return cnt

    

if __name__ == '__main__':
    print(simulate())

