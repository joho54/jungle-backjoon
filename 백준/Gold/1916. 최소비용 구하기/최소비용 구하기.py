#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1916                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1916                           #+#        #+#      #+#     #
#    Solved: 2025/03/29 10:54:48 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
N개의 도시가 있다. 
그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 
우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 
도시의 번호는 1부터 N까지이다.

2. 문제 풀기
이거 다익스트라인데... 먼저 이론을 짚고 넘어가야 합니다.

3. 수도 코드
4. 코드 구현
"""

import heapq, sys
from collections import defaultdict

def dijkstra(G, n ,s):
    # 거리 정보를 무한으로 초기화
    distances = [float('inf') for _ in range(n+1)]
    # 그리고? 스타트 인덱스 초기화 하고 우선순위 큐에 집어 넣기
    distances[s] = 0
    queue = [(s, 0)]
    while queue:
        # current_node, current_distance
        current_node, current_distance = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue

        for neighbor, weight in G[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (neighbor, distance))
    # print(distances)
    return distances

if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())
    buses = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    G = defaultdict(list)
    for u, v, w in buses:
        G[u].append((v, w))
        # G[v].append((u, w))
    start, end = tuple(map(int, input().split()))
    # print(n, m, G, start, end)
    distances = dijkstra(G, n, start)
    print(distances[end])
    