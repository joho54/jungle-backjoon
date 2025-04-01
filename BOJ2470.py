import sys, bisect

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    arr = list(map(int, input().split()))
    arr.sort()
    best_pair = (0, 0)
    best_sum = 2_000_000_000 * 2 # 충~분히 큰 값
    for i in range(n-1):
        target = -arr[i]
        j = bisect.bisect_left(arr, target, i+1, n)
        if j < n: # bisect 특성상 배열 안에 타겟의 베스트 인덱스가 없으면 n을 리턴하므로
            current_sum = arr[i] + arr[j]
            if abs(current_sum) < best_sum:
                best_pair = (arr[i], arr[j])
                best_sum = abs(current_sum)
        # 미세 조정
        if j-1 > i:
            current_sum = arr[i] + arr[j-1]
            if abs(current_sum) < best_sum:
                best_pair = (arr[i], arr[j-1])
                best_sum = abs(current_sum)
    print(best_pair[0], best_pair[1])

if __name__ == '__main__':
    main()

