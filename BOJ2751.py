# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 
# 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 시간제한 2초, 메모리제한 256MB
# 따라서 공간 복잡도가 크고 시간 복잡도가 낮은 알고리즘으로 정렬해야 한다. 기수정렬?
# 입력값을 인덱스로 해서 불 자료형으로 표현하고.
# 그 다음? 순회하면서 출력? 
import heapq
import sys

heap = []

n = int(sys.stdin.readline().strip())  # 빠른 입력

for i in range(n):
    d = int(sys.stdin.readline().strip())  # 빠른 입력

    heapq.heappush(heap, d)

while heap:
    print(heapq.heappop(heap))
