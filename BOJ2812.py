"""
1. 문제 읽기
N자리 숫자가 주어졌을 때, 
여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

2. 문제 풀기

스택 자료구조를 쓰는 거겠지? 그럼 일단 플레인 하게 생각했을 때 스택에 숫자를 차례로 집어 넣고
n은 최대 50만 자리수.

근데 풀이가 생각 안 난다. 유사한 문제? 
가장 작은 자릿수를 뽑아내는 문제? 좀 그리디한 거 같은데.
자릿수 점수? 
안쪽에는 큰 수일수록 좋고
1924
1234
4321

작은 숫자를 구현한다면?

그리디가 맞았다. 스택에 숫자를 넣고, (k개를 덜 지운 상태에서) 현재 숫자보다 큰 숫자가 오면, 
현재 숫자를 빼고 대신 푸시. 똑같이 진행하고
이 과정 끝나고 k 만큼 제거가 안 됐다면 뒤에서부터 제거 <- 왜 이래도 되는지 이해가 잘...
왜냐면 큰 수일수록 앞에 있을 수밖에 없으니까? 사실 잘 납득이 안 간다. 
일단 수도 코드를 작성해보자.

3. 수도 코드
(스택 초기화)
(모든 숫자에 대해 이터레이션한다.)
    (만약 스택이 비어 있으면 그냥 푸시한다.)
    (숫자를 피크와 비교한다.)
    (만약 숫자가 피크보다 크면 )
        (팝하고 대신 넣는다.)
        (카운터를 올린다.)
    (작으면 그냥 넣는다.)
(이터레이션 종료)
(만약 카운터가 K보다 작으면 그만큼 팝 한다.)


4. 코드 구현
"""


from collections import deque

import sys

def solve(nums: list):
    stack = deque()
    cnt = 0
    stack.append(nums[0])
    for num in nums[1:]:
        while stack and stack[-1] < num and cnt < k:
            tmp = stack.pop()
            # print(f'popped {tmp} from stack. now {stack}')
            cnt += 1
        stack.append(num)
        # print(f'appended {num}. now {stack}')
    while cnt < k:
        # print(f'while {cnt} < {k}')
        stack.pop()
        cnt += 1
    return stack

        

if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    nums = list(input().strip())
    result = solve(nums)
    for r in result:
        print(r, end='')
    print()


"""
이슈: 틀렸습니다.

Phase1.
환경: 파이썬
로그: 아래는 정답이 나오는 경우의 로그
7 3
1231234
popped 1 from stack. now deque([])
appended 2. now deque(['2'])
popped 2 from stack. now deque([])
appended 3. now deque(['3'])
appended 1. now deque(['3', '1'])
popped 1 from stack. now deque(['3'])
appended 2. now deque(['3', '2'])
appended 3. now deque(['3', '2', '3'])
appended 4. now deque(['3', '2', '3', '4'])
3234%      

최근 변경 사항: 스택으로 최대 수를 구하는 함수 작성.

Phase2.
확인: 다양한 테스트 케이스 시도하는 방법
오름차순 1234
내림차순 4321
숫자를 하나만 남기고 다 지우는 경우
k가 1이고 n이 2인 경우.
어 뒤에 %기호 뭐지? 생관 없었음.
모든 숫자가 같은 경우. 

찾았다.
10 4
4177252841
477584
정답: 775841임.
해당 케이스의 로그
10 4
4177252841
appended 1. now deque(['4', '1'])
popped 1 from stack. now deque(['4'])
appended 7. now deque(['4', '7'])  <---이떄 왜 비교가 안 일어나지? 아,
그 전에 1이 들어왔어서, 한 번만 비교하고 끝났구나. while로 바꿔야 함.
appended 7. now deque(['4', '7', '7'])
appended 2. now deque(['4', '7', '7', '2'])
popped 2 from stack. now deque(['4', '7', '7'])
appended 5. now deque(['4', '7', '7', '5'])
appended 2. now deque(['4', '7', '7', '5', '2'])
popped 2 from stack. now deque(['4', '7', '7', '5'])
appended 8. now deque(['4', '7', '7', '5', '8'])
appended 4. now deque(['4', '7', '7', '5', '8', '4'])
appended 1. now deque(['4', '7', '7', '5', '8', '4', '1'])
while 3 < 4
477584

시도: 
아래 조건문을 루프로 전환
if stack[-1] < num and cnt < k:
    tmp = stack.pop()
    # print(f'popped {tmp} from stack. now {stack}')
    cnt += 1
stack.append(num)
--->
while stack and stack[-1] < num and cnt < k:
    tmp = stack.pop()
    # print(f'popped {tmp} from stack. now {stack}')
    cnt += 1
stack.append(num)
분석: 성공
"""