"""
1. 문제 읽기 
그냥 재귀를 하는데, 후위는 빠져나올 때 프린트 하면 됨.
그런데 입력이 전위순회 결과라서. 아 그냥 빈 배열 하나 만들고, 
전위 순회 타이밍에 그냥 삽입하면 안 되나, 안 된다. 완전 이진 트리가 아니다!

2. 문제 풀기

3. 수도 코드

4. 코드 구현
"""

import sys


def post_search(idx: int):
    global arr
    """크기가 n인 배열의 idx 번째 요소를 후위순회 합니다."""
    # 만약 왼쪽 자식이 존재 하면
    if idx >= len(bt): return
    post_search(idx*2+1)
    post_search(idx*2+2)
    if bt[idx] != 0: print(bt[idx])


def insert_binary_tree(val: int):
    global bt
    if bt[0] == 0: 
        bt[0] = val # 첫 번째 값 삽입
        return
    ptr = 0
    while True:
        if val < bt[ptr]: # 왼 자식으로 삽입
            if bt[ptr*2+1] != 0: # 왼쪽 자식이 존재하면 그쪽으로 포인터 이동
                ptr = ptr*2+1
                continue
            else: #왼쪽 자식이 없으면 거기에 삽입
                bt[ptr*2+1] = val
                break
        elif val > bt[ptr]: # 오른 자식으로 삽입
            if bt[ptr*2+2] != 0:
                ptr = ptr*2+2
                continue
            else:
                bt[ptr*2+2] = val
                break


arr = []
for line in sys.stdin:
    # line은 '\n'을 포함하므로 line.strip()으로 개행 제거
    arr.append(int(line.strip()))

n = len(arr)
bt = [0]*(n**2) # 모두 양의 정수만 입력됨
for a in arr:
    insert_binary_tree(a)

post_search(0)


"""
이슈: binary search tree에 값 인서트가 이상하게 됨
Phase1.
환경: 파이썬
로그: '50', '30', '98', '24', '5', '52', 0, 0, '28', '45', 0, 0, '60'
최근 변경 사항: 이진트리 삽입 부분 구현

def insert_binary_tree(val: int):
    print(f'inserting: {val}')
    global bt
    if bt[0] == 0: 
        bt[0] = val # 첫 번째 값 삽입
        return
    ptr = 0
    while True:
        if val < bt[ptr]: # 왼 자식으로 삽입
            if bt[ptr*2+1] != 0: # 왼쪽 자식이 존재하면 그쪽으로 포인터 이동
                ptr = ptr*2+1
                continue
            else: #왼쪽 자식이 없으면 거기에 삽입
                bt[ptr*2+1] = val
                break
        elif val > bt[ptr]: # 오른 자식으로 삽입
            if bt[ptr*2+2] != 0:
                ptr = ptr*2+2
                continue
            else:
                bt[ptr*2+2] = val
                break
Phase2.
확인: 오른쪽 자식으로 가는 부분이 좀 이상한 거 같은데. 문자열을 그대로 쑤셔박으니 그렇지!

moving to left child
current ptr: 1
5 > 30
inserting 5 as right child of 30

로그 확인 결과 이런 기가막힌 연산을 하고 있었음을 확인. 이건 그냥 디버거 봤으면 더 빨리 캐치했을 거 같기도 하고.
이슈방지위원회, 줄여서 이방위를 열어야겠다.
시도: 정수형으로 입력값 캐스팅
결과: 해결

이슈: 후위순회가 안 돼요
Phase1. 
환경: 파이썬
로그: 잘못된 후위 순위 검색 결과
최근 변경 사항: 없음

Phase2.
확인: 재귀 과정을 확인하고, 출력문을 찍으면 좋을 적절한 타이밍을 탑다운 방식으로 분석해보기.
시도
결과 분석

"""