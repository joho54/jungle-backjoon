def fibo(n):
    A = [None for _ in range(n)]
    A[0], A[1] = 1, 1
    for i in range(2, n):
        A[i] = A[i-1] + A[i-2]
    print(A)

# 

# 
def fibo_recur(n):
    global a, flag
    if n == 1:
        return 1
    if n == 0:
        return 1
    val = fibo_recur(n-1)  + fibo_recur(n-2)
    if flag[n] == False:
        a.append(val)
        print(f'appending {val}')
        flag[n] = True
    return val
    
    
    
n = 10

a = []
flag = [False for _ in range(n+1)]
# fibo(50)
fibo_recur(10)
print(a)
