from datetime import datetime
import sys


if __name__ == '__main__':
    input = sys.stdin.readline
    start_date = tuple(map(int, input().split()))
    end_date = tuple(map(int, input().split()))
    start_date_time = datetime(start_date[0], start_date[1], start_date[2])
    end_date_time = datetime(end_date[0], end_date[1], end_date[2])
    if start_date[0] + 1000 <= 9999:
        try:
            dooms_day = datetime(start_date[0]+1000, start_date[1], start_date[2]) 
        except ValueError:
            dooms_day = datetime(start_date[0]+1000, start_date[1], start_date[2]-1) 
        if end_date_time >= dooms_day:
            print('gg')
        else:
            time_delta = end_date_time - start_date_time
            print('D-' + str(time_delta.days))        
    else: # 이 경우 단순 출력만 하면 됨.
        time_delta = end_date_time - start_date_time
        print('D-' + str(time_delta.days))        
"""
이슈: value error
확인: d(start_date[0] + 1000, start_date[1], start_date[2]) 여기서 윤년이면 value error가 날 수 있음. 비교 날짜가 문제가 됨.
시도: 먼저 1000을 더해보고, 에러가 나면 start_date[2]에서 1을 뺀 값으로 다시 시도. 왜냐하면 (시작년+1000 = 윤년이 아닌 해,2,29)에서 value error가 났을
테니까.
결과분석: 실패.
왜 실패하지? 3.1. 같은 경우, 1이 0으로 되면서 문제가 될 수 있음. -> 이건 말도 안 되는 케이스. 애초에 어떤 해의 1일이든 문제가 될 수 없음. 
반례를 도저히 모르겠음. 처음부터 start_date_time, end_date_time이 문제인 경우? 그건 입력이 잘못 주어지는 거니까 코드 문제가 아니지.
이거 대체 왜 틀리는 거야. 아니 애초에 value error를 assert로 처리해도 value error로 빠지는 이유는 뭐지?
"""
