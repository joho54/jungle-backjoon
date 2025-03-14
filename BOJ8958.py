t = int(input())
for _ in range(t):
    string = input()
    score = 0
    tmp = 0
    for s in string:
        if s == 'X':
            tmp = 0
        else: 
            tmp += 1
            score += tmp
    print(score)