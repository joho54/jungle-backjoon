"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""
import sys

def init_usetime(k, arr):
    use_time = [0 for _ in range(k+1)]
    # 나머지를 무한대로 초기화하고.
    for elem in arr:
        use_time[elem] += 1
    return use_time
    
def greedy(n, k, arr):
    use_time = init_usetime(k, arr)
    # 이제 힙에는 elem에 대해 (use_time[elem], elem)을 집어 넣으면 됨.
    # 첫 n개의 elem을 집어넣고 시작해야 함.
    multi_tab = set()
    idx = 0 # 고려한 물건 인덱스. 문제가 해결될 때까지 incremental 1 based.
    cnt = 0
    while len(multi_tab) < n:
        if arr[idx] not in multi_tab:
            multi_tab.add(arr[idx])
            use_time[arr[idx]] -= 1
        idx += 1

    for idx_pass2 in range(idx, k):
        if arr[idx_pass2] in multi_tab:
            use_time[arr[idx_pass2]] -= 1
        else:
            # 적절한 최소 인덱스를 찾기
            min_val = float('inf')
            min_idx = 0
            for i in range(1, k+1):
                if use_time[i] < min_val and i in multi_tab:
                    min_idx = i
                    min_val = use_time[min_idx]
            target_idx = min_idx
            multi_tab.remove(target_idx)
            multi_tab.add(arr[idx_pass2])
            use_time[arr[idx_pass2]] -= 1
            cnt += 1
    return cnt
    
    
def test():
    n, k = 2, 7
    arr = (2, 3, 2, 3, 1, 2, 7)
    assert greedy(n, k, arr) == 2
    n, k = 1, 5
    arr = (1, 2, 3, 4, 5)
    assert greedy(n, k, arr) == 4
    n, k = 2, 5
    arr = (1, 2, 1, 2, 3)
    assert greedy(n, k, arr) == 1
    n, k = 3, 7
    arr = (4, 4, 3, 1, 3, 1, 2)
    assert greedy(n, k, arr) == 1
    n, k = 3, 14
    arr = (1, 4, 3, 2, 5, 4, 3, 2, 5, 3, 4, 2, 3, 4)
    assert greedy(n, k, arr) == 4

def submit(greedy):
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    arr = tuple(map(int, input().split()))
    print(greedy(n, k ,arr))

if __name__ == '__main__':	
    # submit(greedy)
    test()

