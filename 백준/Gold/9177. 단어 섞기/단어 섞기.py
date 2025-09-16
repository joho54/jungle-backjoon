# 라벨: 단어 순서를 유지한체로 단어를 만들 수 있는가? 이게 부문제 문제로 어떻게 치환이 되지? -> 그래프로는 어떻게 풀지 알겠음

import sys

def lcs(a: str, b: str):
    dp = [[0]*(len(a)+1) for _ in range(len(b)+1)]

    for i in range(1, len(b)+1):
        for j in range(1, len(a)+1):
            # 가로 세로 각각 보면서
            incr = 0
            if  a[j-1] == b[i-1]:
                incr = dp[i-1][j-1] + 1
            dp[i][j] = max(dp[i][j-1], dp[i-1][j], incr)
    # for row in dp:
    #     print(row)
    return dp[len(b)][len(a)] # 이게 항상 최대일 수밖에 없음.
    

def solve(a, b, c):
    # 그냥 a,c, b,c의 lcs를 각각 찾는 문제였음.
    # 글자 집합이 일치하는지 확인
    map1, map2 = dict(), dict()
    for elem in a:
        if elem in map1:
            map1[elem] += 1
        else: map1[elem] = 0
    for elem in b:
        if elem in map1:
            map1[elem] += 1
        else: map1[elem] = 0
    for elem in c:
        if elem in map2:
            map2[elem] += 1
        else: map2[elem] = 0
        
    # 집합이 같은지 어떻게 알지? 
    if map1 != map2:
        return False
        
        
    return  len(a) ==  lcs(a, c) and len(b) == lcs(b, c)
    

if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input().strip())
    for i in range(t):
        a, b, c = input().split()
        print(f'Data set {i+1}: {'yes' if solve(a, b, c) else 'no'}')
            