import heapq
import sys

a = []

heapq.heapify(a)

n = int(sys.stdin.readline().strip())
for _ in range(n):

    x = int(sys.stdin.readline().strip())
    if x == 0:
        try:
            print(-heapq.heappop(a))
        except IndexError:
            print(0)
    else:
        heapq.heappush(a, -x)