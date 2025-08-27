'''
issue: 65 퍼센트에서 틀림. 
Phase 1.
확인: 예각 삼각형일 경우 아래와 같이 변 길이를 정렬하면 a가 가장 작은 변이 돼버림. 둔각일 때는 그 반대. 
일단 이등변 삼각형의 경우는 의미를 다시 분기시켜서 하위 연산을 해야 함.
```
return sorted([a, b, c])
```

시도: 아래와 같이 분기 구문을 추가
```
        if a == b: 
            a, b, c = a, b, c
        elif b == c:
            a, b, c = b, c, a
        elif a == c:
            a, b, c = a, c, b
```
결과 분석: 해결
'''

import sys, math

def get_edges(points: list):

    x, y, z = points
    a = math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
    b = math.sqrt((y[0]-z[0])**2 + (y[1]-z[1])**2)
    c = math.sqrt((z[0]-x[0])**2 + (z[1]-x[1])**2)

    return sorted([a, b, c])

def solve(points: list):
    a, b, c = get_edges(points)

    if a + b == c:
        print('X')
    elif a == b and b == c:
        print("JungTriangle")
    elif a == b or b == c or a == c:
        if a == b: 
            a, b, c = a, b, c
        elif b == c:
            a, b, c = b, c, a
        elif a == c:
            a, b, c = a, c, b
        pita = math.sqrt(a**2 + b**2)
        if c == pita:
            print('Jikkak2Triangle')
        elif c > pita:
            print("Dunkak2Triangle")
        elif c < pita:
            print("Yeahkak2Triangle")
    elif a != b and b != c and c != a:
        pita = math.sqrt(a**2 + b**2)    
        if c == pita:
            print('JikkakTriangle')
        elif c > pita:
            print("DunkakTriangle")
        elif c < pita:
            print("YeahkakTriangle")

if __name__ == '__main__':
    input = sys.stdin.readline
    points = [
        tuple(map(int, input().split()))
        for _ in range(3)
    ]
    solve(points)