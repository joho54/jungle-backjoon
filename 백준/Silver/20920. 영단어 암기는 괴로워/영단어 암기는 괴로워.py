import sys

def custom_sort(word): # 인자값을 하나만 넣고, asc이라면 그대로, desc라면 -를 붙이면 됨
    return (-mapper[word], -len(word), word)

def solve(words: list, m: int):
    global mapper
    mapper = {}
    for word in words:
        if word not in mapper:
            mapper[word] = 1
        else:
            mapper[word] += 1
    word_set = list(set(words))
    word_set.sort(key=custom_sort)
    ans = []
    for word in word_set:
        if len(word) >= m:
            ans.append(word)
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    words = [
        input().strip()
        for _ in range(n)
    ]
    for ans in solve(words, m):
        print(ans)