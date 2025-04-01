import hashlib
from typing import Any

class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table = [None] * capacity
        
    def hash_value(self, key: Any):
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity
    
    def find(self, key: Any):
        hash = self.hash_value(key=key)
        p = self.hash_table[hash]
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        return False
    
    def add(self, key: Any, value: Any):
        hash = self.hash_value(key)
        p = self.hash_table[hash]
        while p is not None:
            if p.key == key:
                return False
            p = p.next
        temp = Node(key, value, self.hash_table[hash]) # 기존 첫 요소를 내 뒤로 설정.
        self.hash_table[hash] = temp # 내가 일등 먹음. 각 해쉬의 마지막 요소는 next가 None
        return True
    
    def remove(self, key: Any):
        hash = self.hash_value(key)
        p = self.hash_table[hash]
        pp = None
        while p is not None:
            if p.key == key: # 일치하는 키를 찾았을 경우
                if pp is None: # 앞 요소가 none일 경우, 그대로 p만 배제
                    self.hash_table[hash] = p.next
                else: # 앞 요소가 있을 경우!
                    pp.next = p.next # 끝인가?
                return True
            pp = p # 왜 저장해? 끊고 나서 next를 서로 엇갈리게 지정해줘야 함.
            p = p.next
        return False
    
    def dump(self):
        for i in range(self.capacity): #그니까.
            p = self.hash_table[i] # 이터레이션을 어떻게 함?
            print(f'{i}', end='')
            while p is not None:
                print(f'-> {p.key} ({p.value})', end='')
                p = p.next
            print()

if __name__ == "__main__":
    ch = ChainedHash(10)
    ch.add('234', '안녕하세요. ㅎㅎ.')
    ch.add('2344', '안녕하세요. ㅎㅎ.')
    ch.add('2344234', '안녕하세요. ㅎㅎ.')
    ch.add('234423423423', '안녕하세요. ㅎㅎ.')
    ch.add('234423423423234234', '안녕하세요. ㅎㅎ.')
    ch.add('2334', '안녕하세요. ㅎㅎ.')
    ch.add('1111', '안녕하세요. ㅎㅎ.')
    ch.remove('2344234')
    ch.dump()
    print(ch.find('2341111'))
    