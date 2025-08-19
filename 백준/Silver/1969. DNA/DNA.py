import sys

mapper = {0:'A', 1:'C', 2:'G', 3:'T'}

def get_distance(character, genes:list, i: int):
    dist = 0
    for gene in genes:
        if gene[i] != character:
            dist += 1
    return dist

def solve(n: int, m: int, genes: list) -> tuple:
    ans_gene = ''
    total_distance = 0
    for i in range(m):
        freq = [0, 0, 0, 0] # A, C, G, T 
        for j in range(n):
            if genes[j][i] == 'A': freq[0] += 1
            if genes[j][i] == 'C': freq[1] += 1
            if genes[j][i] == 'G': freq[2] += 1
            if genes[j][i] == 'T': freq[3] += 1
        idx = freq.index(max(freq))
        ans_gene += mapper[idx]
        total_distance += get_distance(mapper[idx], genes, i)
    return ans_gene, total_distance

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m  = tuple(map(int, input().split()))
    genes = [
        input().strip()
        for _ in range(n)
    ]
    
    ans_gene, ans_n = solve(n, m, genes)
    print(ans_gene)
    print(ans_n)

"""
5 8
TATGATAC
TAAGCTAC
AAAGATCC
TGAGATAC
TAAGATGT
"""
