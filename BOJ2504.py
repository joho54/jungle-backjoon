"""
1. 문제 읽기: 괄호 안에 숫자가 들어가는 건 아님

2. 문제 풀기
(() [ [] ]) ( [] )
(2+3*3)*2 + 3*2
22 + 6 = 28
오케이 일단 손으로는 풀린다.
일단 이거 열릴 때 푸시하고, 닫힐 때 팝하고, 기본 그 문제에서 조건만 추가해서 
연장한 거 같은데.
일단 만약 비었는데 닫는 괄호가 오면 무조건 0 출력하면 됨.
그리고 팝 하면서 일단 2점인지 3점인지만 판단해도 뭐...
그냥 수식을 직관적으로 계산하는게 좋지 않겠나.
tmp = 1
tmp *= 2
tmp *= 3 이런 식으로
그러다가 스택이 비면 tmp = 1.
일단 푸시 팝 동작이 발생할 때 로그를 찍어서 값을 적절히 조합해서 디버깅해나가자.

이게 기본인데, 여기서 점수를 어떻게 관리하느냐가 관건.스택이 두개 있어야 하나? -일단 해결
스택의 관점에서 계산 값이 어떤게 오느냐에 따라 곱셈과 덧셈을 구별.

풀었다!
스택 사이즈를 유지하고, 팝 후에 스택 사이즈가 이전에 팝 할때 기록한 사이즈와 같으면 덧셈
줄었으면 곱셈
3. 수도 코드
(스택을 이용해괄호 점수를 계산하는 함수)
    (스택을 만듧니다. 세 개 스택 필요. 계산 스택)
    (입력 길이만큼 이터레이션 합니다)
        (아래 스택은 (, [에 대해 각각 유지합니다.)
        (만약 열린 괄호가 온다면)
            (스택에 푸시합니다.)
        (만약 닫힌 괄호가 온다면)  
            (만약 스택이 비어 있다면)  
                (아묻따 0을 리턴합니다.)
            (스택에서 팝 합니다.)
            (팝을 할 때 계산 스택의 사이즈를 검사하고)
                (같으면 값을 더하고)
                (줄었으면 값을 곱합니다.)


4. 코드 구현
"""

from collections import deque
import sys

def solve(parenthesis: list):
    stack1 = deque()
    stack2 = deque()
    stack3 = deque()
    size = 0 # 팝 당시 계산 스택의 사이즈를 기록합니다.
    result = 0
    for p in parenthesis:
        if p == '(':
            stack1.append(p)
            stack3.append(2)
        elif p == ')':
            if not stack1: return 0
            stack1.pop()
            val = stack3.pop()
            if len(stack3) == size:
                result += val
            elif len(stack3) < size:
                pass
        if p == '[':
            stack2.append(p)
            stack3.append(3)
        elif p == ']':
            if not stack2: return 0
            stack2.pop()
        print(f'p: {p}, {result}')
    return 1

if __name__ == '__main__':
    input = sys.stdin.readline
    parenthesis = list(input().strip())
    print(parenthesis)
    print(solve(parenthesis))