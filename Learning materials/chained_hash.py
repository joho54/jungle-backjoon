from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next
    
class ChainedHash:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [None] * self.capacity
    
    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value # 검색 성공
            p = p.next # 뒤쪽 노드를 주목.
        return None # 검색 실패

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next
        
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp # 노드를 추가
        return True # 추가 성공
    
    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key) # 삭제할 key 의 해시값.
        p = self.table[hash] # 노드를 주목
        pp = None # 바로 앞의 노드를 주목

        while p is not None:
            if p.key == key: # key를 발견하면 아래를 실행
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True # 키 삭제 성공
            pp = p
            p = p.next # 뒤쪽 노드를 주목
        return False
    
    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()