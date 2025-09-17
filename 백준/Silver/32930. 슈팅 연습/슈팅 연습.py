# label: 자료구조(최대힙)이 아니다. 기준인 거리가 계속 달라짐.

import sys

def get_next(current_point: tuple, targets: list):
    point_next = (0, 0) # 임의의 초기화
    max_distance = -sys.maxsize
    for target in targets:
        curr_distance = ((target[0] - current_point[0]) ** 2) + (target[1] - current_point[1]) ** 2
        if curr_distance > max_distance:
            point_next = target
            max_distance = curr_distance
    score = max_distance
    return point_next, score

def solve(loop: int, target_now: list, target_next: list):
    ans = 0
    current_point = (0, 0)
    for i in range(loop):
        point_next, score  = get_next(current_point, target_now)
        ans += score
        current_point = point_next
        target_now.remove(point_next)
        target_now.append(target_next[i])
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    target_now = [
        tuple(map(int,input().split()))
        for _ in range(n)
    ]
    target_next = [
        tuple(map(int,input().split()))
        for _ in range(m)
    ]
    
    print(solve(m, target_now, target_next))
        
    
        