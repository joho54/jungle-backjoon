
n = int(input())
arr = list(map(int, input().split()))
max_val = 0

def update_max(new_val):
    global max_val
    if new_val > max_val: max_val = new_val

def pick(i, A):
    if(i == n): 
        update_max(calc(A))
        return
    for idx in range(n): 
        if arr[idx] not in A:
            pick(i + 1, [*A, arr[idx]])

def calc(A):
    tmp = 0
    for i in range(1, n):
        tmp += abs(A[i-1] - A[i])
    return tmp

pick(0,[])  
print(max_val)