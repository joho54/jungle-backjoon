# Phase1. 문제 읽기: 이해했어
# Phase2. 문제 머리로 풀어보기: 26 2+6=8 -> 68, 6+8=14 -> 84, 8+4=12->42, 4+2=6->26!,
# Phase3. 수도코드 작성하기
# Phase4. 구현하기

def calc(n: int, initial_n: int, depth):
    """stringify and get list from the n and get processed num"""
    # base condition
    # print(n)
    if initial_n == n and depth != 0:
        print(depth)
        return
    n = list(map(int, list(str(n))))
    last_n = n[-1]
    processed = sum(n)
    last_proc = processed%10
    pass_n = int(f'{last_n}{last_proc}')

    calc(pass_n, initial_n, depth+1)

n = int(input())
calc(n, n, 0)
