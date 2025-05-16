def solve(word: str):
    ptr = 0
    n = len(word)
    check_list = set()
    while(ptr < n):
        if word[ptr] not in check_list:
            check_list.add(word[ptr])
        else:
            # 안에 있지만 연속된 단어라면
            if word[ptr] == word[ptr-1]:
                pass
            else:
                return False
        ptr += 1
    return True

import sys

if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input())
    ans = 0
    for _ in range(n):
        if solve(input().strip()):
            ans += 1
    print(ans)
