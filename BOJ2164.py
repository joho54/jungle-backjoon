"""
1. 문제 읽기
이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다.
우선, 제일 위에 있는 카드를 바닥에 버린다.
그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
하나는 버리고 하나는 밑으로 보내는 문제

2. 문제 풀기
1 2 3 4
1. 2 3 4
2. 3 4 2
3. 4 2
4. 2 4
5. 4

while 한장만 남을 때까지
홀수 시도에는 그냥 디큐
짝수 시도에는 디큐한 다음 인큐.

3. 수도 코드
4. 코드 구현
"""

from collections import deque

n = int(input())
deck = deque()
for i in range(n):
    deck.appendleft(i+1)
i = 1
while len(deck) > 1:
    tmp = deck.pop()
    if i % 2 == 0:
        deck.appendleft(tmp)
    i+=1

print(deck[0])