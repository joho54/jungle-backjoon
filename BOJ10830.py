"""
1. 문제 읽기
2. 문제 풀기
divide and conquer로 풀어야 한다. base case는 분명히 그거.
제곱만 하면 돼서
일단 그래보자. 아닌가.
그럼 수도코드를 작성해보자.
3. 수도 코드
(함수: 재귀적으로 dot product, 인수: 행렬 a, 제곱수 b)
    (base case: 만약 b가 2라면)
        (a by a dot product하고 바로바로 1000모듈러 연산 후)
        (리턴: 위에서 구한 a제곱%b)
    (recursion case)
    (temp=recur(a, b//2)) # 재귀로 구한 행렬 결과에 대해,
    (result = 1로 초기화된 a와 위상이 같은 행렬)
    result = recur(temp, 2)%b # 한번 더 재곱을 해 주면 됨.(상수 시간 보장)
    (만약 b가 홀수라면: result에 대해 a를 dot product 해줘야 함.)
        result = (이건 그냥 여기 dot product 코드를 작성하는게 제일 빠르겠다.)
    return result

4. 코드 구현
"""
import sys

def dot_product(a: list, b: list, n: int):
    """do dot product on identically shaped matrices"""
    result = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
                # print(f'{result[i][j]} += {a[i][k]} * {b[k][j]}')
            result[i][j] %= 1000
    return result

def recur(a: list, b: int):
    if b == 1:
        result = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]
        for i in range(n):
            for j in range(n):
                result[i][j] = a[i][j] % 1000
        return result
    # b가 0일 수 있나? 0은 1//2일 때만 0이 나오는데, 그건 아마 불가능할건데.
    # 근데 저거, 2일때도 안 해도 되지 않나? ㅇㅇ 
    # 근데 여전히 틀렸다고 함.
    # 여기가 주 재귀
    temp = recur(a, b // 2) # 선형 재귀
    # 여기는 temp 결과에 대한 재귀
    result = dot_product(temp, temp, n) # 상수시간
    if b%2 == 1:
        """do result^a"""
        result = dot_product(result, a, n) # 상수 시간.
    return result

if __name__ == '__main__':
    input = sys.stdin.readline
    n, b = tuple(map(int, input().split()))
    matrix = [tuple(map(int, input().split())) for _ in range(n)]
    result = recur(matrix, b)
    for row in result:
        for elem in row:
            print(elem, end=' ')
        print()

"""
이슈: 80프로에서 틀렸습니다.

Phase1.
환경: 파이썬
로그: 틀렸습니다.
최근 변경 사항: 행렬 제곱 분할정복 코드 작성

Phase2.
확인: 80프로면 뭘 확인해야 하지? 
(그런데 확실히 수도코드 다 작성하고 코딩하니까 빠르긴 하다. 40분 걸려서 80프로 맞는 코드를 쓰긴 했으니)
다음 테스트케이스를 발견(질문 게시판)
2 1 (2 by 2 행렬을 1제곱하는 테스트케이스, 각 원소의 최대값은 1000이므로 합리적인 범위)
1000 1000
1000 1000
결과
1000 1000 
1000 1000
정답은 당연히 모든 행렬이 0이어야 함. 그런데 바닥 조건에서 다음과 같이 처리하는 바람에
if b == 1:
    return a
결과가 위와 같이 나오게 됨.(dot_product 함수가 실행되지 않으면 모듈러 연산을 거칠
기회가 없음!)

시도: 행렬 제곱이 1회여도 모듈러 연산을 하도록 수정
if b == 1:
    result = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            result[i][j] = a[i][j] % 1000
    return result
분석: 성공. 곱셈과 너무 유사해서 쉽게 풀 수 있었다.
"""