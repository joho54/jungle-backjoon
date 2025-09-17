import heapq

def min_classrooms(lectures, mapper: dict):
    # lectures는 (start, end) 튜플 리스트
    lectures.sort(key=lambda x: x[1])  # 시작 시간 기준 정렬
    min_heap = []  # 강의실 별 끝나는 시간 관리
    total_room = 0
    
    for idx, start, end in lectures:
        if min_heap and min_heap[0][0] <= start:
            room_num = min_heap[0][1]
            mapper[idx] = room_num # DEBUG: 매퍼 지정 시 힙에 삽입 후 하게 되면 인덱스가 바뀌게 됨
            heapq.heapreplace(min_heap, (end, room_num))  # 가장 빨리 끝나는 강의실에 배정, 종료시간 갱신
        else:
            total_room += 1
            heapq.heappush(min_heap, (end, total_room))  # 새 강의실 추가
            mapper[idx] = total_room
    return len(min_heap)


import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    lectures = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    mapper = {}
    print(min_classrooms(lectures, mapper))
    ordered_key = sorted(mapper.keys())
    for key in ordered_key:
        print(mapper[key])
