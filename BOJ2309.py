# 난쟁이를 완전 탐색으로 찾아야 함. 그냥 빼기 빼기 하는 식으로 하면 되지 않나? 
# 아 그냥 다 더하고 두개씩 차례로 빼면 n^2에 찾을 수 있음
dwarfs = [
    int(input())
    for _ in range(9)
]

def find_dwarfs(dwarfs):
    sum_val = sum(dwarfs)
    for i in range(len(dwarfs)):
        dwarf1 = dwarfs[i]
        for j in range(i+1, len(dwarfs)):
            dwarf2 = dwarfs[j]
            if sum_val - dwarf1 - dwarf2 == 100:
                return sorted([dwarf for dwarf in dwarfs if dwarf != dwarf1 and dwarf != dwarf2])
for dwarf in find_dwarfs(dwarfs=dwarfs):
    print(dwarf)

