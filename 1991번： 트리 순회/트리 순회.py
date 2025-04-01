#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1991                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1991                           #+#        #+#      #+#     #
#    Solved: 2025/03/27 21:04:08 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


"""
1. 문제 읽기: ok
2. 문제 풀기: DFS로 다 풀면 될 거 같음.
그런데 아무리 고민해도 머리속에 구현이 안 나온다. 이거 입력 어떻게 처리했는지 하나도 기억이 안 남.
3. 수도 코드: 
4. 코드 구현
"""

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder(node: Node):
    # base case
    if node == None:
        return
    print(node.value, end='')
    # 왼쪽 먼저.
    if node.left != None:
        preorder(node.left)
    if node.right != None:
        preorder(node.right)

def inorder(node: Node):
    # base case
    if node == None:
        return
    if node.left != None:
        inorder(node.left)
    print(node.value, end='')
    if node.right != None:
        inorder(node.right)

def postorder(node: Node):
    # base case
    if node == None:
        return
    if node.left != None:
        postorder(node.left)
    if node.right != None:
        postorder(node.right)
    print(node.value, end='')


def get_adjacency_array(arr: list):
    pass

import sys

if __name__ == '__main__':
    
    input = sys.stdin.readline
    n = int(input().strip())
    arr = [
        tuple(map(str, input().split()))
        for _ in range(n)
    ]
    nodes = {}
    for val, left, right in arr:
        if val not in nodes:
            nodes[val] = Node(val)
        if left != '.':
            if left not in nodes:
                nodes[left] = Node(left)
            nodes[val].left = nodes[left]
        if right != '.':
            if right not in nodes:
                nodes[right] = Node(right)
            nodes[val].right = nodes[right]
    preorder(nodes['A'])
    print()
    inorder(nodes['A'])
    print()
    postorder(nodes['A'])
    