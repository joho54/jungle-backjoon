"""
1. 문제 읽기: 
2. 문제 풀기: 일단 문제 목표가 뭔지는 알겠는데, 이것도 이진 탐색하고 무슨 상관인지 모르겠다.
양 끝에 인덱스 공유기를 잡고, 가운데 값을 이진 탐색해서 위치를 잡으면 안 되나?
1 2 4 8 9
일때
1, 9는 그냥 공유기를 배치하고, 또 left, right인덱스로 잡고 이진 탐색 시작.
다음으로 할 일은, (1+9)//2=5가 있는지 탐색. 만약 있으면 거기 설치. 그러면
최소 거리가 4, 4가 되어 최선의 값을 구할 수 있음
그러나 없을 수도 있다. 
그러면? 왼쪽, 오른쪽으로 한 번 더 이진 검색. 이때, 결정트리 상에서 오른쪽을 먼저 갈지
왼쪽을 먼저 갈지만 정하되, 양 쪽 다 가기는 해야 한다. 이런 걸 수도코드로 해본적이 없어서
잘 모르겠다. 
아 그리고 집 좌표 배열은 검색만 하면 되므로 해시 사용!
3. 수도 코드
routers = []
s = deque()
while left <= right:
    center = (left+right)//2
    if dictionary.get(center, -1) != -1: # 센터 값이 있으면
        routers.append(dictionary[center]) # 일단 값에 추가하고
        break
    # 센터 값이 없으면?
    # 결정 트리를 분기해서 이진탐색을 해야 한다. 왼쪽 자식을 먼저 가기 위해 오른쪽을 저장
    if center+1 <= right: s.append((center+1, right)) # 오른쪽 분기 저장
    if left <= center: s.append((left, center)) # 왼쪽 분기 저장
    # 최상단 값 팝.
    if s:
        left, right = s.pop()
        continue
    break
    
이게 작동할지는 의문. 일단 코드는 이렇다. 이걸 문제 설계에 맞게 집어넣어야 함.
그런데 이게 중요한게, 결정 트리에서 왼쪽 자식과 오른쪽 자식을 다 보고 넘어가야 하는데?
최하단 값을 팝 하면 안 되나
자료구조가 어떻게 디지?
dictionary[idx] = True
이렇게는 또 못 푼다 뭔가 prefix sum 같은걸 이용해야하나? 문제 갈피를 못 잡겠다.
    
4. 코드 구현

"""

import sys
from collections import deque

n, c = tuple(map(int, sys.stdin.readline().split()))
dictionary = {}
for i in range(n):
    dictionary[i] = int(sys.stdin.readline().strip())

left = min(dictionary.values())
right = max(dictionary.values())

routers = []
s = deque()
while left <= right:
    center = (left+right)//2
    if dictionary.get(center, False): # 센터 값이 있으면
        routers.append(center) # 일단 값에 추가하고
        break
    # 센터 값이 없으면?
    # 결정 트리를 분기해서 이진탐색을 해야 한다. 왼쪽 자식을 먼저 가기 위해 오른쪽을 저장
    if center+1 <= right: s.append((center+1, right)) # 오른쪽 분기 저장
    if left <= center: s.append((left, center)) # 왼쪽 분기 저장
    # 최상단 값 팝.
    if s:
        left, right = s.popleft()

        continue
    break
    

"""
이슈: 
"""