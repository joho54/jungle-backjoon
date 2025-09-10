import sys

'''
1 2 5 -> 1
1 4 5 -> 3
2 3 5 -> 1
'''

if __name__ == '__main__':
    input = sys.stdin.readline
    
    n = int(input().strip())
    arr = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    dic = dict()
    for i, x, c in arr:
        if x-i not in dic:
            dic[x-i] = c
        else:
            dic[x-i] += c
    print(max(dic.values()))
        
        