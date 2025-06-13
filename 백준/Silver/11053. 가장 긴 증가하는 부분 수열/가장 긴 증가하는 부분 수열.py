"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
요소를 이터레이션하면서, temp에서 요소가 들어갈 최적 위치를 찾아서, 배열 안에 존재하면 
덮어 써버리고, 밖에 존재하면 배열을 늘여서 LIS를 구할 수 있음.
4. 코드 구현
"""
import sys, bisect

input = sys.stdin.readline
n = int(input().strip())
arr = tuple(map(int, input().split()))

tmp = [arr[0]]

for x in arr:
    # print(f'iterating: {x}')
    i = bisect.bisect_left(tmp, x, 0, len(tmp))
    # print(f'{i} = bisect.bisect_left({tmp}, {x}, 0, {len(tmp)})')
    if i == len(tmp):
        # print(f'tmp.append({x})')
        tmp.append(x)
    else:
        # print(f'{tmp[i]} = {x}')
        tmp[i] = x

# print(tmp)
print(len(tmp))