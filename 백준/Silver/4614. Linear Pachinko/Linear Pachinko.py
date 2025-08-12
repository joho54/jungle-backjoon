import sys
            

def simulate(i: int, pachinko: str, momentum=None) -> bool:
    n = len(pachinko)
    while True:
        if not (i >= 0 and i < n):
            return 100
        if pachinko[i] == '/': 
            if momentum is None:
                momentum = 'L'
                i -= 1
                if i >= 0 and i < n:
                    continue
                else: 
                    return 100
            else:
                return 0
        
        elif pachinko[i] == "\\":
            if momentum is None: 
                momentum = 'R'
                i += 1
                if i >= 0 and i < n:
                    continue
                else:
                    return 100
            else: 
                return 0
        
        elif pachinko[i] == '.':
            return 100
        
        elif pachinko[i] == '_':
            if momentum is None:
                return 0
            elif momentum == 'L':
                i -= 1
                if i >= 0 and i < n:
                    continue
                else:
                    return 100
            elif momentum == 'R':
                i += 1  
                if i >= 0 and i < n:
                    continue
                else:
                    return 100
        
        elif pachinko[i] == '|':
            if momentum is None:
                result1 = simulate(i+1, pachinko, momentum='R')
                result2 = simulate(i-1, pachinko, momentum='L')
                return ((result1 + result2) // 2)
            else:
                return 0

def solve(pachinko):
    # /\.|__/\.
    if len(pachinko) == 0: return None
    total = 0
    for i in range(len(pachinko)):
        total += simulate(i, pachinko)
    
    return total//len(pachinko)

if __name__ == '__main__':
    input = sys.stdin.readline
    while True:
        pachinko = input().strip()
        if pachinko ==  "#": break
        print(solve(pachinko))
        