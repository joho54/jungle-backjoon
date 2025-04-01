"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
일단 각 동물에 대해 이터레이션 하면서, 
    만약 동물이 y값부터 멀면 제외
    동물 위치 x값으로 사대 x값들을 이진 탐색으로 찾아서(사대 정렬 필요)
    만약 해당하는 사대가 있으면 카운트
4. 코드 구현
"""

import sys, bisect

input = sys.stdin.readline
m, n, l = tuple(map(int, input().split()))
step = list(map(int, input().split()))
animals = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def solve():
    step.sort()
    cnt = 0
    for animal in animals:
        x, y = animal
        # print(f'animal: {x}, {y}')
        if y <= l: 
            # print(f'at least {y} <= {l}')
            i = bisect.bisect_left(step, x, 0, len(step))
            # print(f'do bisect.bisect_left({step}, {x}, 0, {len(step)})->{i})')
            if i == len(step): i -= 1
            # print(f'valid step: {step[i]}')
            if (abs(x-step[i])+y) <= l:
                # print(f'get_distance({x}, {y}, {step[i]}) -> True')
                # print(f'got an animal! cnt = {cnt} + 1')
                cnt += 1
            # else: print(f'get_distance({x}, {y}, {step[i]}) -> False')
        # else: print(f'out of y range')
    return cnt

if __name__ == '__main__':
    print(solve())