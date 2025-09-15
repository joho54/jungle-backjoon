# 라벨: 자료구조(어렵지 않은데 어렵네. 집합을 써야 하나.)
# 이기는 구간을 정리하는게 첫 번째 작업인 거 같습니다.  

import sys

def calculate_lap(calc_tuple: tuple):
    start, end = calc_tuple
    sm, ss = map(int, start.split(':')) 
    em, es = map(int, end.split(':'))
    sts = ss + sm*60
    ets = es + em*60
    tts = ets-sts
    return tts

def convert_tts(tts: int):
    pm = tts//60
    ps = tts%60
    spm = str(pm) if len(str(pm)) == 2 else f'0{pm}'
    sps = str(ps) if len(str(ps)) == 2 else f'0{ps}'
    return spm + ':' + sps
    
    
    

def solve(n: int, records: list):
    start = '00:00'
    end = '48:00'
    prev = start
    win_map = {1:0, 2:0, 3:0}
    calc_map = {1:[], 2:[], 3:[]}
    prev_win = None
    records.append((3, end))
    # 모든 기록을 순회
    for record in records:
        # 1, 10:00
        # 이긴 팀 정보와 시점을 조회
        team_num, lap = record
        team_num = int(team_num)
        # 새롭게 이긴 팀 기록을 계산
        win_map[team_num] += 1
        # 현재 결과 업데이트
        if win_map[3] == 1: # 만약 게임 끝이면
            win_team = 3
        elif win_map[1] > win_map[2]:
            win_team = 1
        elif win_map[1] < win_map[2]:
            win_team = 2
        else:
            win_team = None
        # 만약 새로이 이기는 팀과 이전에 이긴 팀이 다르고, 이전 팀이 유효하다면 계산 맵에 이전 승리 팀을 추가.
        if prev_win in (1, 2):
            calc_map[prev_win].append((prev, lap))
        prev = lap
        # 이전 승리 팀을 현재 승리 팀으로 갱신
        prev_win = win_team
    ans_map = {1:0, 2:0}
    for elem in calc_map:
        for lap in calc_map[elem]:
            ans_map[elem] += calculate_lap(lap)
    
    for elem in ans_map:
        ans_map[elem] = convert_tts(ans_map[elem])
        print(ans_map[elem])

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    records = [
        input().split()
        for _ in range(n)
    ]
    solve(n, records)