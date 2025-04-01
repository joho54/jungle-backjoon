"""
1. 문제 읽기
이거 딱봐도 그 그리디 문제인데. 못 박는 문제랑 강의실 배정이랑 비슷하다.
2. 문제 풀기
강의실 문제는 기억이 나는데(늦게 끝나는 강의 순으로 우선 배정), 못 박는 문제는 기억이 안난다.
못은? 아 진짜 기억이 안 나네.
x 좌표 상에 선들의 위치가 주어졌을 때, 가장 많은 선을 못으로 관통할 경우 선의 개수를 구하라.
문제는 이거고, 정답은? 못의 위치를 옮겨가며 관통하는 선 최대 수를 완전탐색으로 구했던 거 같은데
(이건 그리디가 아니잖아 그럼.)
아무튼, 문제를 보자.
못이랑 비슷하게 철로가 시작하는 지점을 incremental하게 시뮬레이션하고,
철로가 끝나는 지점 안으로 범위 안의 선들이 들어오면 정답에 더해주기?
여기서 힙을 어떻게 쓰지? 아, 못이 최대한 많이 박히는 지점들을 그리디하게 구해서, 
그 최대 지점들을 커버하면 되는 거 아닌가?
이것도 아닌 거 같다. 문제를 이해하지 못하겠다.
강의실 배정 문제의 역발상인 거 같기도 하고?
특정 지점을 못 박기 문제처럼 구한 다음, 강의실 문제처럼 그리디하게 구하되, 
빨리 시작하는 지점부터 보면서 조건에 따라 수에 추가하면? 일단 그래볼까? 아니 근데 그러면, 
모든 h, o 쌍에 대해 선을 그려본다는 의미고, 
그 각각의 이터레이션 동안 최악 n개의 선이 범위 안에 있는지 판단해야 하니까
h, o 범위만 따져도 -100,000,000~100,000,000이고 철로 길이는 200,000,000에다가,
각 집의 최대 개수는 100,000이니까, 200,000,000 * 100,000의 복잡도가 나온다.
이러면 안 될텐데.

•	구간을 “end” 기준으로 순회하면서,
그 완전탐색을 하긴 하는데, end 기준으로 역으로 올라가면서 그리디하게 보는 문제다.
만약 구간이 d보다 아예 크면 배제
end-d, end에서 end 큰 순으로 정렬해서, 힙에 집어넣고, 
end-d가 start이해 됨? 올랑말랑.
일단 루프를 돌며너
(모든 집회사 구간에 대해 루프: start, end로 생각)
    start가 end-d보다 큰 경우, 이 구간은 포함시킬 수 있음
    일단 대충 알겠음.


3. 수도 코드

(모든 구간을 (start, end), (start<end) 형식으로, end에 대해 오름차순으로
정렬하여 배열로 저장)

(함수: 그리디하게 철로로 커버할 수 있는 구간을 구하는 함수)
    (힙을 생성)
    (첫 번째 구간을 푸시)
    (첫 번째 구간을 제외한 모든 영역을 end 기준으로 이터레이션(end 기준으로 오름차순 정렬했으니 당연))
        (만약 start, end 차가 d보다 크지 않다면)
            (현재 구간의 end는 힙 내에서 최고값임! 따라서 지금 가정할 수 있는 철로 구간은 아래와 같음)
            (end-d ~ d)
            (일단 아묻따 현재 구간을 푸시. 왜? 지금은 현재 구간 기준으로 철로 깔 거니까 현재 구간은 무조건 포함(철로보다 짧은 구간임은 이미 확인))
            (현재 힙의 루트는? start가 가장 작은 값 = end-d 구간에 못 들어갈 확률이 가장 높은 구간)
            (while: 위 논리에 의거해 루트의 start가 end-d보다 커질 때까지 팝)
            (heap에 대한 정리가 끝난 다음 max heap size를 갱신.)

4. 코드 구현
"""

import heapq
import sys

def greedy(pairs):
    h = []
    max_h = 0
    heapq.heapify(h)
    start, end = pairs[0]
    if end - start <= d: 
        heapq.heappush(h, pairs[0])
    for i in range(1, len(pairs)):
        start, end = pairs[i]
        if end - start <= d: 
            heapq.heappush(h, (start, end))
            root = heapq.heappop(h)
            while root[0] < end - d:
                root = heapq.heappop(h)
            heapq.heappush(h, root)
        max_h = max(len(h), max_h)
    return max_h


if __name__ == '__main__':
    input = sys.stdin.readline
    n  = int(input().strip())
    pairs = []
    for _ in range(n):
        start, end = tuple(map(int, input().split()))
        start, end = (end, start) if end < start else (start, end)
        pairs.append((start, end))
    pairs.sort(key=lambda x: x[1])
    d  = int(input().strip())
    print(greedy(pairs))
    
    
