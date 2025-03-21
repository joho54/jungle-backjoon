import sys

MAX_VAL = 10_001

n = int(sys.stdin.readline().strip())
f = [0 for _ in range(MAX_VAL)] 
max_d = 0
for _ in range(n):
    d = int(sys.stdin.readline().strip())    
    max_d = max(max_d, d)
    f[d] += 1



cnt = 0
for i in range(max_d+1):     
    while f[i] > 0:
        print(i)
        f[i] -= 1
        cnt += 1
        
    

    

