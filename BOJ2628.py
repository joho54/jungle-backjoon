# Phase1. 문제 읽기
# 문제 자체는 간단하다. 종이를 잘랐을 때, 최대가 되는 넓이를 구하는 거다.
# 그런데 메서드가 문제다. 
# Phase2. 문제 풀기
# 종이를 자르고 난 후 각 영역의 파티션 넓이를 구한다.
# 다른 방법은? 뭐가 있지? 자르는 부분을 알고 있을 때 최대 넓이를 구하는 방법은? 
# 일단 너무 문제를 크게 생각하고 있다. 작게 생각하자
# 주어진 값
# 세로 컷: 4
# 가로 컷: 2, 3
# 여기서 가로세로의 파티션 구하는 방법
# 세로컷 구하는 이니셜 이런 모양. {0,4,가로길이}
# 프리픽스 섬 필요 없음. 이니셜 -> 파티션으로 하면 됨.
# 이니셜 {0, 2, 3, 세로길이(8)}
# 파티션 [2-0, 3-2, 8-3] = [2, 1, 5]

def get_partition_from_initial(initial: list):
    partition = [0 for _ in range(len(initial)-1)]
    for i in range(len(partition)):
        partition[i] = initial[i+1] - initial[i]
    return partition

width, height = tuple(map(int, input().split()))

n = int(input())
w_initial = [0, width]
h_initial = [0, height]
for _ in range(n):
    code, point = tuple(map(int, input().split()))
    if code == 1: w_initial.append(point)
    if code == 0: h_initial.append(point)

w_partition = get_partition_from_initial(sorted(w_initial))
h_partition = get_partition_from_initial(sorted(h_initial))
max_width = 0
for w in w_partition:
    for h in h_partition:
        max_width = w*h if w*h > max_width else max_width
print(max_width)
