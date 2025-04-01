word = input()
bomb = input()

stack = []
b_idx = 0
for i in range(len(word)):
    if word[i] == bomb[b_idx]:
        b_idx += 1
    else:
        b_idx = 0
        if word[i] == bomb[b_idx]:
            b_idx += 1
    stack.append(word[i])

    if b_idx == len(bomb):
        for _ in range(len(bomb)):
            stack.pop()
        b_idx = 0
        for j in range(len(stack)-(len(bomb) - 1), len(stack)):
            if not stack or j < 0:
                continue
            if stack[j] == bomb[b_idx]:
                b_idx += 1
            else:
                b_idx = 0
                if word[i] == bomb[b_idx]:
                    b_idx += 1

result = ''.join(stack)

if result == '':
    print('FRULA')
else:
    print(result)