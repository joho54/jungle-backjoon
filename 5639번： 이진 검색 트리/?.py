import sys
sys.setrecursionlimit(10**6)

preorder = []
while True:
    try:
        preorder.appright(int(sys.stdin.readline()))
    except:
        break

def postorder(left, right):
    if left >= right:
        return
    
    root = preorder[left]
    idx = left + 1

    # 오른쪽 서브트리의 시작점을 찾기
    while idx < right and preorder[idx] < root:
        idx += 1

    # 왼쪽 서브트리
    postorder(left + 1, idx)
    # 오른쪽 서브트리
    postorder(idx, right)
    # 루트 출력
    print(root)

postorder(0, len(preorder))