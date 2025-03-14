c = int(input())
for _ in range(c):
    inputs = tuple(map(int, input().split()))
    n, scores = inputs[0], inputs[1:]
    # score avg
    avg = sum(scores)/len(scores)
    # get people over than avg
    superiors = 0
    for score in scores:
        if score > avg:
            superiors+=1
    ans = (superiors/len(scores))*100
    print(f'{ans:.2f}%')
