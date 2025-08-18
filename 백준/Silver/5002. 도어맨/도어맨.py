import sys

'''
1
MWWMWMMWM
'''

def solve(n: int, line: str) -> int:
    result = 0
    women = 0
    men = 0
    while True:
        result = women + men
        if len(line) == 0: 
            break
        if abs(women-men) > n:
            result -= 1
            break
        if women > men:
            if len(line) > 1:
                # skip condition
                if line[0] == 'W' and line[1] == 'M':
                    if len(line) > 2:
                        line = line[0] + line[2:]
                    else:
                        line = line[0]
                    men += 1
                    continue
                else:
                    pass
            else:
                # TODO:
                if abs(men-women) == n:
                    break
                pass
        elif women < men:
            if len(line) > 1:
                # skip condition
                if line[0] == 'M' and line[1] == 'W':
                    if len(line) > 2:
                        line = line[0] + line[2:]
                    else:
                        line = line[0]
                    women += 1
                    continue
                else: 
                    pass
            else:
                # TODO: 스킵을 못 하는 상황이고, 이대로 추가했을 때 최종 조건을 넘는지 검사해야 함.
                # print("TODO")
                if abs(men-women) == n:
                    break
                pass
            
        if line[0] == 'M':
            men += 1
        else:
            women += 1
        line = line[1:]
    print(result)
    
    

if __name__ == '__main__':
    input = sys.stdin.readline
    
    n = int(input().strip())
    line = input().strip()
    solve(n, line)