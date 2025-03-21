# 하노이 원판
# Phase1. 문제 읽기
# 한 번에 하나의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# Phase2. 문제 풀기
# n 20을 기점으로 출력 여부가 달라짐. 
# N 최대값은 100.
# 일단 방법은 알겠거든 그런데 리컬젼을 어떻게 해야 할지 모르겠다. 
# move_plate(i): i번째 원판을 옮긴다 쳐. 
# 그다음 재귀는? move_plate()
# 순서를 바꿔서 종료조건부터 생각해보자. 
# 원판 = [1,2,3]
# hanoi = [[1, 2, 3], [], []]
# 다음 = [[2, 3],[],[1]]
# ...
# = [[][][1, 2, 3]]
# 이렇다. 
# 종료조건은  len(hanoi[2])==3
# recursion할 때 들어가야 하는 정보는? 원판 번호, 다음 위치, 
# 다음 위치는 뭔데. 
# recursion. 결국 작은 문제를 해결하는 방식으로 큰 문제가 해결되는 건데. 
# Phase3.  문제는 풀겠다. 그런데 머리로는 아무것도 안 돌아간다. 더 n=4를 다시 풀어복.
# Phase4. 재귀 코드 템플릿을 작성해보기
# 모르겠다. 일단 25분 이상 생각했다.
# 자 이제 다시 생각해보자. recursion 에서 중요한 건 sub problem 정의하는 거다. 
# 사실 그림 이해하면 끝이긴 하다.

# 그러면 어떻게 하는데. 
global_n = int(input())
ans = 0
# n개의 원판을 start에서 end로 옮기는 경로.
def move(no: int, x: int, y: int) -> None:
	global global_n, ans
	if no > 1:
		move(no - 1, x, 6 - x - y)
	print(x, y) if global_n <= 20 else None
	ans += 1
	if no > 1:
		move(no - 1, 6 - x - y, y)

move(global_n, 1, 3)
print(ans)
