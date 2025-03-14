import math

# 숫자 n보다 작은 모든 자연수를 이터레이팅 하면서 그 수가 소수인지 판별하고, 그 소수 값 p로 n - p 한 값이 소수면 리스트에 등록.
# 시간 초과 문제. 

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

def get_goldbach(is_prime):
    number = int(input())
    for i in range((number//2), 1, -1): # number //2 이렇게 반 까지만 보고, 가장 값이 큰 i를 기준으로 출력하면 되지 않겠나.
        if is_prime(i) and is_prime(number - i):
            return (i, number-i) # 전체 순회하지 말고 최선의 속도로 답을 찾은 다음 함수를 리턴 시켜야 문제를 풀 수 있었음.

n = int(input())
for _ in range(n):
    print(*get_goldbach(is_prime))
