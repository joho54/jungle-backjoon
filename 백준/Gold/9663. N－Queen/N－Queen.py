import sys

n = int(sys.stdin.readline().strip())

flag_a = [False for _ in range(n)]
flag_b = [False for _ in range(2 * n - 1)]
flag_c = [False for _ in range(2 * n - 1)]

Queens = [None for _ in range(n)]
cnt = 0

def recur(i):
    global cnt
    for j in range(n):
        if (flag_a[j] == False
            and flag_b[i+j] == False
            and flag_c[n - 1 + i - j] == False
            ):
            Queens[i] = j
            if i == n-1:
                cnt += 1
                continue
            flag_a[j] = True
            flag_b[i+j] = True
            flag_c[n - 1 + i - j] = True
            recur(i + 1)
            flag_a[j] = False
            flag_b[i+j] = False
            flag_c[n - 1 + i - j] = False

recur(0)
print(cnt)