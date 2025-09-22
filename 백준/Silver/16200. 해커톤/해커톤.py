# 9
# 2 2 2 3 3 3 2 2 2
# 오름차순 정렬, 뒤쪽 영역 커버하기
# 2 2 2 2 2 2 3 3 3
# 1 2 3 4 5 6 7 8 9


# label: 정렬

import sys

def solve(n: int, arr: list):
    arr.sort()
    idx = 0
    team_cnt = 0
    
    # 첫 번째 팀 
    pivot_num = arr[idx]
    team_cnt += 1
    
    while  idx < n:
        pivot_num -= 1
        if pivot_num == 0: 
            idx += 1
            if idx < n:
                pivot_num = arr[idx] # 다음 최소 팀원 수를 설정
                team_cnt += 1 # 그 다음 팀 카운트 시작
        else: 
            idx += 1
    
    return team_cnt

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    arr = list(map(int, input().split()))
    print(solve(n, arr))