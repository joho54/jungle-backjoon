"""
1. 문제 읽기: 이해가 어렵진 않음
2. 문제 풀기: 생각보다 어려움. 아래처럼 하면 될 거 같은데 시간초과 남. 
복잡도를 계산해서 더 나은 방식으로 풀어야 함.
3. 수도 코드
이거 어떻게 풀더라. 힙을 두 개 만들고, 새로운 애를 루트와 비교해서 
민힙과 맥스힙을 유지하는데, 민힙은 항상 맥스힙보다 1 많게. 
민힙의 루트와 맥스힙의 루트를 비교하고, 만약 맥스힙 쪽이 더 크면 민힙 루트와 스왑
크기 규칙을 초과해도 옮겨주고 스왑.
일단 다 민 힙으로 몰아 넣어주기

4. 코드 구현
"""
import sys

import heapq


def solve():
    n = int(sys.stdin.readline().strip())
    # 루트가 right힙보다 크다면 스왑
    left_heap = [] # right_heap보다 1 크거나 같게. 
    right_heap = []
    left_l, right_l = 0, 0
    heapq.heapify(left_heap) # min heap!
    heapq.heapify(right_heap) # max heap!
    for _ in range(n):
        x = int(sys.stdin.readline().strip())
        # print(f'input value: {x}')
        heapq.heappush(left_heap, -x)
        left_l += 1
        # print(f'initially pushing it to left heap: {left_heap}, size: {left_l}')
        if left_l-2 == right_l:
            # print(f'left heap got bigger: {left_l} v {right_l}')
            heapq.heappush(right_heap, (-heapq.heappop(left_heap)))
            left_l -= 1
            right_l += 1
            # print(f'now balanced: {left_heap}, {right_heap}')
        if right_l > 0:
            # compare
            left_root = -heapq.heappop(left_heap)
            right_root = heapq.heappop(right_heap)
            # print(f'comparing {left_root}  vs {right_root}')
            if left_root > right_root:
                # should be replaced
                left_root, right_root = right_root, left_root
                # print(f'swapped')
            heapq.heappush(right_heap, right_root)
            heapq.heappush(left_heap, -left_root)
            # print(f'after swapping: {left_heap}, {right_heap}')
        else:
            # right heap이 존재하지 않을 경우
            left_root = -heapq.heappop(left_heap)
            # 그냥 기록만 하고 저장
            heapq.heappush(left_heap, -left_root)
        
        print(left_root)
solve()


        
"""
이슈: 1,2,3 입력 시 에러

Phase1.
환경: 파이썬
로그

10
1
input value: 1
initially pushing it to left heap: [1], size: 1
1
2
input value: 2
initially pushing it to left heap: [1, 2], size: 2
left heap got bigger: 2 v 0
now balanced: [2], [-1]
comparing 2  vs 1
swapped
after swapping: [1], [-2]
1
3
input value: 3
initially pushing it to left heap: [1, 3], size: 2
comparing 1  vs 2
after swapping: [1, 3], [-2]
1

최근 변경 사항: min heap, max heap을 이용한 구현

Phase2.
확인: 1,2,3 일때, 1, 2가 왼쪽에, 3이 오른쪽에 들어가야 하는데, 힙 특성상
그렇게 안 되고 있음.
어떻게 하는데 그럼? 
3 넣을 때, 일단 1, 3 / 2가 되고, 여기서...그럼 오른쪽이 min heap이어야 하는 거 아냐?

1 이거 밸런스 맞출 때도 큰 쪽을 밑에 넣고 (그럼 맥스값이고)
2

1 3 이때는? 3과 2 비교해서 스왑
2

1 2
3

-1 1  이렇게 되고. 그지?
3 2

그럼 위쪽이 맥스힙, 아래쪽이 민힙이어야 한다.
시도: 그렇게 바꿔줌
분석: 성공인듯?
"""