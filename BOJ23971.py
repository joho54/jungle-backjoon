"""
1. 문제 읽기
그냥 그리디 같은데.
2. 문제 풀기
그런데 거의 수학 문제다. 수학적으로 풀어야 한다.
어떻게 수학적으로 풀지? 
한가지 assumption: 첫 번째 사람은 무조건 1, 1에 앉는다. 
그러면, 나머지 사람은 그냥 위치가 정해지지 않나? 
세로로 n명 가로로 m명,
무식하게 풀면? (n + 1) + (n + 1) + (n + 1) + n ... n < H
0 + ?*(n+1) < H
1+1 = 2
so
? * 2 < 5
? <= 5/2 = 2.5 -> 3
1+1 = 2
so
? * 2 < 4 
? <= 2
그냥 반올림 하면 되는 건가? 반올림의 의미가 뭐지? 한 영역이 2라고 했을때 그 2가 다 들어오지 않아도 상관 없다는 뜻.
H = 7,
n = 1
ans = 4
1+1 = 2
7/2 = 3.5

good

3. 수도 코드
4. 코드 구현
"""

import sys

def solve(h, w, n, m):
    vert = h//(n+1) + 1 if h % (n+1) != 0 else h//(n+1)
    hor = w//(m+1) + 1 if w % (m+1) != 0 else w//(m+1)
    return vert * hor

def submit(solve):
    input = sys.stdin.readline
    h, w, n, m = tuple(map(int, input().split()))
    print(solve(h, w, n, m))

def test():
    h, w, n, m = 5, 4, 1, 1
    assert solve(h, w, n, m) == 6

if __name__ == '__main__':
    submit(solve)
    # test()
