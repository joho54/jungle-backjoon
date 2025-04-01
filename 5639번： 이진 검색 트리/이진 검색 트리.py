#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5639                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5639                           #+#        #+#      #+#     #
#    Solved: 2025/03/27 21:51:32 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
50
30
24
5
28
45
98
52
60
아 스택을 활용하면 되나?

3. 수도 코드
4. 코드 구현
"""

import sys
from collections import deque

class Node:
    def __init__(self, value=None, left=None, right=None, predecessor=None):
        self.value = value
        self.left = left
        self.right = right
        self.predecessor = predecessor


def solve(nodes: list):
    global root_node
    root = nodes[0]
    root_node = prev = Node(value=root)
    
    for i in range(1, len(nodes)):
        current = Node(value=nodes[i])
        if current.value < prev.value:
            prev.left = current
            current.predecessor = prev
            # print(f'{current.value} <--- {prev.left.value}')
        elif current.value > prev.value:
            prev.right = current
            current.predecessor = prev
            prev = prev.predecessor
            # print(f'{current.value} ---> {prev.value}')
    return root

def post_order(node: Node):
    if node == None: return
    post_order(node.left)
    post_order(node.right)
    print(node.value)


if __name__ == "__main__":

    nodes = []
    for line in sys.stdin:
        nodes.append(int(line.strip()))
    root_node = None
    solve(nodes=nodes)
    post_order(root_node)
    
