#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9251                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9251                           #+#        #+#      #+#     #
#    Solved: 2025/04/04 12:45:39 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def get_lcs(a: list, b: list):
    dp = [[0 for _ in range(len(b))] for _ in range(len(a))]
    # init
    tmp = 0
    # 세로 문자열
    for i in range(0, len(a)):
        if a[i] == b[0]: 
            tmp = 1 
        dp[i][0] = tmp
    
    tmp = 0
    for i in range(0, len(b)):
        if b[i] == a[0]: 
            tmp = 1 
        dp[0][i] = tmp 

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            tmp = 0
            if a[i] == b[j]:
                tmp = dp[i-1][j-1] + 1
            # else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], tmp)

    return dp[-1][-1]

def test():
    a = "ACAYKP"
    b = "CAPCAK"
    assert get_lcs(a, b) == 4
    a = "abc"
    b = "cde"
    assert get_lcs(a, b) == 1
    a = "abcc"
    b = "cdec"
    assert get_lcs(a, b) == 2
    a = "ECGIJEH"
    b = "JHHEAGF"
    assert get_lcs(a, b) == 2

def submit(get_lcs, input):
    a = list(input().strip()) 
    b = list(input().strip())
    print(get_lcs(a, b))

if __name__ == '__main__':	
    input = sys.stdin.readline
    submit(get_lcs, input)
    # test()