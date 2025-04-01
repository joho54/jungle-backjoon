"""
1. 문제 읽기
이해가 어렵지는 않음. 그런데 왜 스택 문제인지 잘 모르겠음.
스택: 선입선출
이 문제에서 선입선출의 대상은? 원? 원을 먼저 푸시한다고 해봐? 
원 안에 원이 있는지 원 밖에 있는지를 알면 되는 거 아닌가? 그걸로 categorization이 
될 거 같은데.
find 함수로 원 안의 원을 찾아서 재귀적으로 스택을 써야할 것으로 보임.
일단 떠오르는 코드를 구현해보까?
2. 문제 풀기
3. 수도 코드
전체 배열을 유지
첫 번째 원을 작업스택에 푸시한다.
푸시한 원 안의 원이 존재하는지 전체 배열을 검사한다.
존재한다면 전체 배열에서 제거하고 작업 스택에 푸시한다.
같은 작업을 반복한다.
꺼내면서 영역을 검사한다? 잘 하면 될 거 같은데? base circle이라는 개념이 있어야 하지 않겠나.
원을 뽑으면서 카운터 1 증가시키면 되지 뭐. 
그리고 find로 안에 있는거 다 찾고 뽑으면서 검사하는 거고.
그러니까 모든 원에 대해 스택 연산을 하긴 해야 하는 거다. 나의 수도 코드대로면
n 은 300,000이라서 좀 크긴 한데.
이거 아닌거 같아.
4. 코드 구현
이
"""

from collections import deque

n = int(input())
circles = [[]]*n
for i in range(n):
    x, r = tuple(map(int, input().split()))
    circles[i] = (x-r, r+x)
print(circles)



def find_inner(circle: tuple):
    """원 circle보다 안에 있는 원의 리스트를 완전 탐색으로 찾아서 리턴합니다."""
    ans = []
    for circle_target in circles:
        if circle == circle_target: continue
        # 찾았다면
        if circle[0] <= circle_target[0] and circle_target[1] <= circle[1]:
            ans.append(circle_target)
    return ans

def solve():
    for circle in circles:
        stack = deque()
        stack.append(circle)
        while stack:
            c = stack.pop()
            inner_circles = find_inner(c)
            for c2 in inner_circles:
                stack.append(c2)
            print(f"inner circles of {c}: {inner_circles}")
            """이러면 스택을 쓸 이유가 없지!"""

solve()

"""
이슈
Phase1.
Phase2.
"""