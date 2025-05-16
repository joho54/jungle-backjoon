import sys

def solve(coins, k):
    idx = len(coins)-1
    cnt = 0
    while True:
        # 현재 가리키는 동전이 전체 값보다 작을 때까지 포인터 감소
        while k < coins[idx]:
            idx -= 1
        # 이제 k보다 동전 값이 작습니다. 동전 값보다 k가 큰 동안만
        # while k >= coins[idx]:
        #     k -= coins[idx]
        #     cnt += 1
        r = k//coins[idx]
        k -= coins[idx]*r
        cnt += r
        if k == 0:
            return cnt

if __name__ == '__main__':	
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    coins = [
        int(input().strip())
        for _ in range(n)
    ]
    print(solve(coins, k))
