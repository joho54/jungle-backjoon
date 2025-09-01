import sys

def solve(pw: str):
    vowel_streak, consonant_streak = 0, 0
    general_streak = 0
    vowel_cnt = 0
    vowels = {'a', 'i', 'u', 'e', 'o'}
    consonant = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l','m','n','p','q','r','s','t','v','w','x','y','z'}
    prev = None
    for alpha in pw:
        # 1번 조건: 모음 하나 이상
        if alpha in vowels: 
            vowel_cnt += 1
        # 2번 조건: 3개 연속 자음 or 모음
        if alpha in vowels:
            vowel_streak += 1
            consonant_streak = 0
        elif alpha in consonant:
            consonant_streak += 1
            vowel_streak = 0
        
        if vowel_streak >= 3 or consonant_streak >= 3: return False 
        
        # 3번 조건: 같은 문자 3번 이상 안 됨
        if prev is not None and prev == alpha and alpha not in {'e', 'o'}:
            general_streak += 1
        else:
            general_streak = 0
        prev = alpha
        if general_streak >= 1: return False
        
    # 검사 종료 후 검증
    if vowel_cnt == 0: return False
    return True

if __name__ == '__main__':
    input = sys.stdin.readline
    while True:
        pw = input().strip()
        if pw == 'end': break
        result = solve(pw)
        if result:
            print(f'<{pw}> is acceptable.')
        else:
            print(f'<{pw}> is not acceptable.')