import hashlib
from typing import Any
from enum import Enum

class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2

class Bucket:
    def __init__(self, key: Any = None, value: Any = None, stat: Any = 'EMPTY'):
        self.key = key
        self.value = value
        self.stat = stat
    
    def set_status(self, stat):
        self.stat = Status[stat]
    
    def __str__(self):
        return f"[{self.key}]={self.value}, stat: {self.stat}"

class OpenHash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [Bucket()]*capacity

    def __str__(self):
        string = ''
        for t in self.table:
            string += f'[{t.key}]={t.value}, status: {t.stat}\n'
        return string
    
    def hash_value(self, key):
        if isinstance(key, int):
            return key%self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16)%self.capacity
    
    def rehash_value(self, key):
        return (self.hash_value(key) + 1) % self.capacity
    
    def search_node(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]
        print(f'initial node p: {p}')
        for i in range(self.capacity): #이터레이션 목적이 뭐지? 해쉬 테이블에서 키값을 찾기 위함.
            print(f'node p: {p}')
            while p.stat != 'EMPTY': 
                if p.stat == 'OCCUPIED' and p.key == key: #OCCUPIED이고 키가 일치한담면. p는 버킷임.
                    return p
            hash = self.rehash_value(key)
            p = self.table[hash]
        print(f'search_node({key}): Failed to find it.')
        return False

    def search(self, key):
        p = self.search_node(key)
        if p is None:
            return p.value
        return False
    
    def add(self, key, value):
        p = self.search_node(key)
        if p is not False: 
            return False # 키가 이미 존재
        print(f'{key} does not exist in hash. proceeding...')
        # 해시 구하기
        hash = self.hash_value(key)
        # 버킷에 주목. 
        p = self.table[hash]
        # 버킷이 차 있는 동안
        while p.stat == "OCCUPIED":
            # 재해시 해야지
            hash = self.rehash_value(key)
            p = self.table[hash]
            print(f'hash: {hash}, p: {p}')
        if not p.stat == "OCCUPIED":
            self.table[hash] = Bucket(key, value, "OCCUPIED")
            return True
        return False
    
    # def remove(self, key):

if __name__ == '__main__':
    os = OpenHash(10)
    print(os.add(234, '난 너를 좋아해~~^0^'))
    print(os.add(234, '난 너를 싫어해 ㅠㅡㅜ~~^0^'))
    print(os.add(3, '난 너를 싫어해 ㅠㅡㅜ~~^0^'))
    print(os.add(23234234234, '난 너를 싫어해 ㅠㅡㅜ~~^0^'))
    print(os.add(2324, '난 너를 싫어해 ㅠㅡㅜ~~^0^'))
    print(os.add('2324', '난 너를 싫어해 ㅠㅡㅜ~~^0^'))
    print('-'*10)
    print(os)




"""
이슈: Enum 관련 에러.

Phase1.
환경: 파이썬
로그: TypeError: module() takes at most 2 arguments (3 given)
최근 변경 사항: 오픈 해시법 구현.

Phase2.
확인: Enum 상속을 잘못 받음
```
import enum, hashlib

class Status(enum):
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2
```
시도: 
올바른 상속
```
from enum import Enum

class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2
```
분석: 해결
"""             
"""
이슈: 버킷 초기화 문제

Phase1.
환경: 파이썬
로그: TypeError: Bucket.__init__() missing 3 required positional arguments: 'key', 'value', and 'stat'
최근 변경 사항: 오픈 해시 구현

Phase2-1
확인: 오픈해시의 버킷 초기화 과정에 key, value, status 인수를 어떻게 설정해야 하는가?
(솔직히 기억 안 남. 책 참조)
책을 보니 그냥 None으로 기본값을 줬다. ㅇㅋ
시도: 
def __init__(self, key: Any = None, value: Any = None, stat: Any = None):
분석: 해결 
"""
"""
이슈: 

Phase1.
환경: 파이썬
로그: 없음(add 호출 시 search_node에서 무한 루프 발생.)
최근 변경 사항: search 함수 구현

Phase2.
확인: search node 함수에 프린트 찍어서 진행상황 추적
시도: 오 성공한듯? 일단 추가 자체는 성공. 중복추가 해보자. 중복추가할 때 그냥 씹히는거 같음. 
그게 제대로된 동작임 ㅇㅇ. 추가는 완료.
분석: 
"""
"""
이슈: 추가 함수를 여러번 실행하면 무한 루프에 빠짐.

Phase1.
환경: 파이썬
로그: 추가 실행 시 무한 루프. 별도 로그 없음
최근 변경 사항: 추가 함수 구현

Phase2.
확인: search 하던 중 멈추는 문제.
시도: 
분석: 
"""
"""컨디션 난조로 지능 이슈 발생. 초초초 머나몸고 공부법으로 가야겠다. 필사! """