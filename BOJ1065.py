# Phase1. 문제 읽기
# 일단 한수가 뭔지는 알겠어. 
# 한수의 갯수에 규칙이 있을 거 같은데.
# Phase2. 문제 풀기
# 110 99
# 일단 100까지 한수는 99로 고정.
# 1, 2, ... 모든 두자릿수, 99
# 100에서 200까지의 한수는?
# 111, 123, 135, 147, 159
# 210까지의 한수는
# 210
# n의 최대값은 1000. 그냥 한수를 찾는 함수를 구하는게 나을지도. 

def is_hansoo(n: int):
    # define wheather is it hansoo or not
    if len(str(n)) < 3: return True
    digits = [int(digit) for digit in str(n)]
    for i in range(2, len(digits)):
        sub1 = digits[i] - digits[i-1]
        sub2 = digits[i-1] - digits[i-2]
        if(sub1 != sub2): return False
    return True

ans = 0
n = int(input())
for i in range(1, n+1):
    if is_hansoo(i): ans+=1
print(ans)