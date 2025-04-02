import sys
sys.setrecursionlimit(10**6)


def post_order(left, right):
    # 리프 노드면 출력을 해줘야 함.
    if left >= right:
        return
    root = nodes[left]
    k = left+1
    while k < right and nodes[k] < root:
        k += 1
    post_order(left+1, k)
    post_order(k, right)
    print(root)

if __name__ == "__main__":

    nodes = []
    for line in sys.stdin:
        nodes.append(int(line.strip()))
    # 루트를 먼저 받는다.
    post_order(0, len(nodes)) # 재귀적으로 서브트리를 정리
"""
post_order(left+1, k-1)
->
post_order(left+1, k)

"""