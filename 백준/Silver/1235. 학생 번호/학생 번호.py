'''
3
1212345
1212356
0033445
'''

import sys

def solve(codes: list, n: int):
    k = 0
    code_len = len(codes[0]) # 전체 문자열 크기 구하기.
    while True:
        tmp_set = set()
        k += 1 # increase k range
        fixed_k = code_len - k
        for code in codes:
            tmp_code = code[fixed_k:]
            if tmp_code not in tmp_set:            
                tmp_set.add(tmp_code)
            else:
                tmp_set = set() # 셋 초기화
        # 여기에 도달했다면 무슨 의미임?
        if len(tmp_set) == n:
            break
    return k

if __name__ == '__main__':
    input = sys.stdin.readline
    
    n = int(input().strip())
    codes = [
        input().strip()
        for _ in range(n)
    ]
    print(solve(codes, n))