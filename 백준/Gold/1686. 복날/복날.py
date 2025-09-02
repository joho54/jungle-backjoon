import sys
import math
from collections import deque

def can_go(prev, next, v, m):
    px, py = prev
    nx, ny = next
    distance = math.sqrt((px-nx)**2 + (py-ny)**2)
    return (distance / v) <= (m * 60)  # m분을 초로 환산하여 비교

def solve(graph, start, end, v, m):
    # 방문 기록: 노드별 최소 경유 벙커 수
    visited = {pos: float('inf') for pos in graph}  
    queue = deque()

    visited[start] = 0
    queue.append((start[0], start[1], 0))  # (x, y, 경유 벙커 수)

    while queue:
        x, y, cnt = queue.popleft()

        if (x, y) == end:
            print(f'Yes, visiting {cnt-1} other holes.')
            return

        for nx, ny in graph:
            if (nx, ny) != (x, y) and can_go((x, y), (nx, ny), v, m):
                # 다음 노드 방문 시 현재보다 더 적은 경유 벙커 수일 때만 추가 탐색
                if visited[(nx, ny)] > cnt + 1:
                    visited[(nx, ny)] = cnt + 1
                    queue.append((nx, ny, cnt + 1))
    
    print("No.")

if __name__ == '__main__':
    input = sys.stdin.read().strip().split('\n')
    v, m = map(int, input[0].split())
    start_x, start_y = map(float, input[1].split())
    end_x, end_y = map(float, input[2].split())
    bunkers = [tuple(map(float, line.split())) for line in input[3:]]

    graph = [(start_x, start_y), *bunkers, (end_x, end_y)]
    solve(graph, (start_x, start_y), (end_x, end_y), v, m)
