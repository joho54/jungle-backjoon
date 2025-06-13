import sys

def solve(n: int):
    divisor = 2
    while True:
        if n % divisor == 0: # divisor로 나눠 떨어지면
            print(divisor)
            n = n // divisor
        else: # 나눠 떨어지지 않으면
            divisor += 1 
        if n == 1:
            break



if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    solve(n)