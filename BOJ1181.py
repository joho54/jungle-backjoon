# # 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 
# # 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.


# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

import sys

words = []
wordset = []
n = int(sys.stdin.readline().strip())
# input 
for _ in range(n):
    word = sys.stdin.readline().strip()
    if word not in wordset:
        words.append([word, len(word)])
        wordset.append(word)

words.sort(key=lambda x: (x[1], x[0]))

for word in words:
    print(word[0])
# 그래서 뭐 해야 하는데? 하나만 남기고 제거하는 걸 먼저 생각해야겠는데? 
# 하나만 남기고 제거 어떻게 해?

