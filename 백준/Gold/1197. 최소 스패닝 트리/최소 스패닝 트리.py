#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1197                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1197                           #+#        #+#      #+#     #
#    Solved: 2025/03/28 13:45:11 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# class Node:
#     def __init__(self, value=None):
#         self.value = value

# class Bucket:
#     def __init__(self, node: Node, next=None, w=None):
#         self.node = node
#         self.next = next
#         self.w = w

# class AdjacencyList:
#     def __init__(self, v_num: int):
#         self.table = [
#             Bucket(Node(i)) for i in range(1, v_num+1)
#         ]

from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)

def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y, c):
    global parent
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        return c
    return 0



if __name__ == '__main__':	
    input = sys.stdin.readline
    v, e = tuple(map(int, input().split()))
    E = [
        tuple(map(int, input().split()))
        for _ in range(e)
    ]
    # 1. 입력받기. 어떻게? 연결 리스트? 
    # 근데 인접 리스트 어떻게 만들어? 그냥 linked list 구현하면 되나?

    # al = AdjacencyList(v)
    # for bucket in al.table:
    #     print(bucket.node.value)
    # 그래프 입력부터 또 막히네. 똑같이 딕셔너리 쓰면 안 되나. 
    # 일단 간선 정보를 어떻게 저장해야할지 모르겠음!!
    E.sort(key=lambda x: x[2])
    parent = [i for i in range(v+1)]
    cost = 0
    for u, v, c in E:
        cost += union(u, v, c)
    print(cost)