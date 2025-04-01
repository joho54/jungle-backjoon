import sys
sys.setrecursionlimit(10**6)

preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

def postorder(start, end):
    if start >= end:
        return
    
    root = preorder[start]
    idx = start + 1

    # 오른쪽 서브트리의 시작점을 찾기
    while idx < end and preorder[idx] < root:
        idx += 1

    # 왼쪽 서브트리
    postorder(start + 1, idx)
    # 오른쪽 서브트리
    postorder(idx, end)
    # 루트 출력
    print(root)

postorder(0, len(preorder))