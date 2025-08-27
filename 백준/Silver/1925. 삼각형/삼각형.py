'''
세 점이 일직선 위에 있으면 - ‘삼각형이 아님’  출력할 때는 X
세 변의 길이가 같으면 - ‘정삼각형’ 출력할 때는 JungTriangle
두 변의 길이가 같으면
가장 큰 각이 90°보다 크면 - ‘둔각이등변삼각형’ 출력할 때는 Dunkak2Triangle
가장 큰 각이 90°이면 - ‘직각이등변삼각형’ 출력할 때는 Jikkak2Triangle
가장 큰 각이 90°보다 작으면 - ‘예각이등변삼각형’ 출력할 때는 Yeahkak2Triangle
세 변의 길이가 모두 다르면
가장 큰 각이 90°보다 크면 - ‘둔각삼각형’ 출혁할 때는 DunkakTriangle
가장 큰 각이 90°이면 - ‘직각삼각형’ 출력할 때는 JikkakTriangle
가장 큰 각이 90°보다 작으면 - ‘예각삼각형’ 출력할 때는 YeahkakTriangle
'''

'''
issue: 65 퍼센트에서 틀림. 
Phase 1.
확인: 예각 삼각형일 경우 아래와 같이 변 길이를 정렬하면 a가 가장 작은 변이 돼버림. 둔각일 때는 그 반대. 
일단 이등변 삼각형의 경우는 의미를 다시 분기시켜서 하위 연산을 해야 함.
```
return sorted([a, b, c])
```

시도: 
결과 분석:
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