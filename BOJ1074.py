import sys
result = 0
def recur(n, x, y, cnt):
    # base condition
    # 알아서 잘 해보시고.
    global result
    if n == 2:
        if r == x and c == y:
            pass
        elif r == x and c == y + 1:
            cnt += 1
        elif r == x + 1 and c == y:
            cnt += 2
        elif r == x + 1 and c == y + 1:
            cnt += 3
        result = cnt
        return cnt
    half = n // 2  # 현재 크기의 절반 (사분면 크기)
    
    if r < x + half and c < y + half:  # 1️⃣ A (좌상) 
        recur(half, x, y, cnt)
    elif r < x + half and c >= y + half:  # 2️⃣ B (우상)
        recur(half, x, y + half, cnt + half * half)
    elif r >= x + half and c < y + half:  # 3️⃣ C (좌하)
        recur(half, x + half, y, cnt + 2 * half * half)
    else:  # 4️⃣ D (우하)
        recur(half, x + half, y + half, cnt + 3 * half * half)

n, r, c = tuple(map(int, sys.stdin.readline().split()))
n = n ** 2
recur(n, 0, 0, 0)
print(result)