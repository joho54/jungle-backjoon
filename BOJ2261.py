"""
1. 문제 읽기
2차원 평면상에 n개의 점이 주어졌을 때, 이 점들 중 가장 가까운 두 점을 구하는 프로그램을 작성하시오.

2. 문제 풀기
좌표평면이니까
좌상에서 제일 가까운 점 사이 거리
우상에서 제일 가까운 점 사이 거리
좌하에서 제일 가까운 점 사이 거리
우하에서 제일 가까운 점 사이 거리
cross에서 제일 가까운 점 사이의 거리?
점이 n개라 할 때 완전탐색 하면 당연히 n^2의 비교를 해야 구할 수 있음.

점 자체를 두 가지 기준으로 정렬하고, 
(x가 작을수록, y가 작을수록)
그 다음에 점들에 대해 분할정복하면 되지 않나? 
왼쪽에서 가장 가까운 점 재귀로 구하고, 
오른쪽에서 가장 가까운 거리 재귀로 구하고
가운데 걸쳐서 가장 가까운 점 컴바인 과정에서 구하고
리턴을 최소값으로 해주면.

아이디어 자체는 이게 맞을 거 같다.

5 -> 2, 3
4 -> 2, 2
3 -> 3
2 -> 2
1 -> 이런 경우 없음

3. 수도 코드

(걸치는 최소를 구하는 함수(left, mid, right))
    (left, right 영역 전체에서 최소 거리 구해주기. 어 이거 히스토그램 사각형이랑 비슷하게 하면 안 되나)
    lo, hi = mid, mid+1
    (오른쪽 점을 선택 했을 때 왼쪽 점을 선택한 경우보다 거리가 줄어든다면)
        (오른쪽으로 갑니다.)
    (그게 아니면 왼쪽으로 갑니다.)
    (이거는 약간 기억에 의존해서 하게 될 거 같긴 한데.)

(재귀적으로 left, right의 영역의 점들에 대해 가장 가까운 점 사이의 거리를 리턴하는 함수)
    (바닥 조건: left+1 == right, 즉, 점이 두 개 있는 상황)
        (두 점 사이의 거리를 상수시간에 구해서 리턴)
    (left == right일수도 있음: 그러면 어떡해야 함? 0을 리턴하면 안 되고. n은 2 이상이니까, 1이 아니라 3인 경우를 봐주면 안 되나.)
    (재귀조건)
    (가운데 인덱스 = (left+right)//2)
    (왼쪽 최소 = 재귀(left, mid))
    (오른쪽 최소 = 재귀(mid+1, right)
    (이제 걸치는 최소(cross_min)을 구해야 함. 이거 복잡하니까 별도의 함수로 빼서 생각하자 일단.)
    (return min(왼쪽 최소, 오른쪽 최소, 걸치는 최소))
        

4. 코드 구현
"""

import sys

def get_cross_min(left, mid, right):
    """mid 를 기준으로 좌 우로 최선의 선택이 되는 동안 점을 선택해서 거리를 리턴"""
    lo, hi = mid, mid + 1
    cross_len = (dots[lo][0] - dots[hi][0])**2 + (dots[lo][1] - dots[hi][1])**2
    while lo > left or hi < right:
        # 왼쪽으로 가는 경우의 길이
        if hi < right and (lo == left or 
                           (dots[lo-1][0] - dots[hi][0])**2 + (dots[lo-1][1] - dots[hi][1])**2
                           >
                           (dots[lo][0] - dots[hi+1][0])**2 + (dots[lo][1] - dots[hi+1][1])**2
                           ):
            hi += 1
            cross_len = min(cross_len, (dots[lo][0] - dots[hi][0])**2 + (dots[lo][1] - dots[hi][1])**2)
        else:
            lo -= 1
            cross_len = min(cross_len, (dots[lo][0] - dots[hi][0])**2 + (dots[lo][1] - dots[hi][1])**2)
    return cross_len

def recur(left: int, right: int):
    """left, right 영역의 점들에 대해 가장 가까운 점 사이의 거리를 리턴한다."""
    if left + 2 == right: # 영역에 점이 세 개일 때.
        a, b, c = dots[left], dots[left+1], dots[right] 
        # 세 점의 거리를 구한다.
        dist_a = (a[0] - b[0])**2 + (a[1] - b[1])**2 # a - b
        dist_b = (a[0] - c[0])**2 + (a[1] - c[1])**2 # a - c
        dist_c = (c[0] - b[0])**2 + (c[1] - b[1])**2 # b - c
        return min(dist_a, dist_b, dist_c)
    if left + 1 == right: # 영역의 점이 둘 일때.
        a, b = dots[left], dots[right]
        return (a[0] - b[0])**2 + (a[1] - b[1])**2
    
    mid = (left+right)//2
    left_min = recur(left, mid)
    right_min = recur(mid+1, right)
    cross_min = get_cross_min(left, mid, right)
    return min(left_min, right_min, cross_min)



if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    dots = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    dots.sort(key=lambda x: (x[0], x[1]))
    # print(dots)
    print(recur(0, len(dots)-1))
    