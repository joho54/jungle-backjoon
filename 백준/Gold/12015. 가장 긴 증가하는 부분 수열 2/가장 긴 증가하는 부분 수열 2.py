import sys
from bisect import bisect_left


def solve(n: int, seq: list) -> int:
    lis = []  # define pseudo lis
    for num in seq:
        pos = bisect_left(lis, num)
        if pos == len(lis):  # if pos is equal to the length of lis
            lis.append(num)  # increase lis itself
        else:  # otherwise
            lis[pos] = num
        # print(lis)
    return len(lis)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().strip())
    seq = tuple(map(int, input().split()))
    print(solve(n, seq))