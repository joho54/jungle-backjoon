"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

import sys

def greedy(n, appliers):
    appliers.sort()
    max_cnt = 0
    for i in range(n-1):
        # pivot
        cnt = 1
        pivot_doc, pivot_interview = appliers[i]
        for j in range(i+1, n):
            comp_doc, comp_interview = appliers[j]
            if pivot_interview > comp_interview:
                cnt += 1
                pivot_doc, pivot_interview = comp_doc, comp_interview
        max_cnt = max(cnt, max_cnt)
    return max_cnt


def greedy_2(n, appliers):
    appliers.sort()
    # pivot
    cnt = 1
    pivot_doc, pivot_interview = appliers[0]
    for j in range(1, n):
        comp_doc, comp_interview = appliers[j]
        if pivot_interview > comp_interview:
            cnt += 1
            pivot_doc, pivot_interview = comp_doc, comp_interview
    return cnt

def test():
    n = 5
    appliers = [(3, 2), (1, 4), (4, 1), (2, 3), (5, 5)]
    assert greedy_2(n, appliers) == 4
    n = 7
    appliers = [(3, 6), (7, 3), (4, 2), (1, 4), (5, 7), (2, 5), (6, 1)]
    assert greedy_2(n, appliers) == 3
    n = 3
    appliers = [(1, 2), (2, 100), (3, 99)] 
    assert greedy_2(n, appliers) == 2

def submit(greedy):
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        appliers = [
            tuple(map(int, input().split()))
            for _ in range(n)
        ]
        print(greedy(n, appliers))

if __name__ == '__main__':	
    # submit(greedy_2)
    test()
