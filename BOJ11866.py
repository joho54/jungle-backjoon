"""
1. 문제 읽기
1 2 3 4 5 6 7
3

2. 문제 풀기
그냥 모듈러 연산 잘 써서 지워주면 될듯
3. 수도 코드
4. 코드 구현
"""

n, k = tuple(map(int, input().split()))
arr = [
    i for i in range(1, n+1)
]
idx = 0
ans = '<'
while arr:
    # print(f'prev idx: {idx}')
    idx = (idx+k-1)%n
    # print(f'{arr}, delete {arr[idx]}')
    ans += f'{arr[idx]}, '
    del arr[idx]
    n -= 1

ans = ans[:-2]+'>'
print(ans)
