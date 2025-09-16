# 라벨: 

def get_duration(start: str, end: str):

    sy, sm, sd = tuple(map(int, start.split('.')))
    ey, em, ed = tuple(map(int, end.split('.')))
    dy = ey - sy
    dm = em - sm
    dd = ed - sd
    dm += dy*12 # do carry
    dd += dm*28 # do carry
    return dd


def solution(today, terms, privacies):
    answer = []
    # term_mapper
    term_mapper = dict()
    for term in terms:
        term_type, term_duration = term.split()
        term_mapper[term_type] = int(term_duration) * 28 # day 기준
        
    for idx, privacy in enumerate(privacies, 1):
        privacy_date, privacy_type = privacy.split()
        # 최소 단위를 day로 잡기
        
        passed_days = get_duration(privacy_date, today)

        if passed_days >= term_mapper[privacy_type]:
            answer.append(idx)
    
    
    return answer