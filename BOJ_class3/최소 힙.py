import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

            
class Heap:

    #속성 생성
    def __init__(self):
        self.heap = []
        self.heap.append(None)

    def check_swap_up(self, idx):
        # 삽입한 모드의 부모 노드가 없을 경우
        if idx <= 1:
            return False
        parent_idx = idx // 2

        if self.heap[idx] < self.heap[parent_idx]:
            return True
        else:
            return False
    
    def insert(self, data):
        self.heap.append(data)
        idx = len(self.heap) - 1

        while self.check_swap_up(idx):
            parent_idx = idx // 2

            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
        
        return True
    
    def check_swap_down(self, idx):
        left_idx = idx * 2
        right_idx = idx * 2 + 1

        #자식 노드가 하나도 없을 경우
        if left_idx >= len(self.heap):
            return False
        
        #자식 노드가 하나일 경우
        if right_idx >= len(self.heap):
            if self.heap[left_idx] < self.heap[idx]:
                return True
            else:
                return False
        
        #자식 노드가 두 개일 경우
        else:
            min_child = min(self.heap[left_idx], self.heap[right_idx])
            if self.heap[idx] > min_child:
                return True
            else:
                return False

    def pop(self):
        idx = len(self.heap) - 1
        self.heap[1], self.heap[idx] = self.heap[idx], self.heap[1]
        data = self.heap.pop()
        idx = 1

        while self.check_swap_down(idx):
            left_idx = idx * 2
            right_idx = idx * 2 + 1

            if right_idx >= len(self.heap):
                if self.heap[left_idx] < self.heap[idx]:
                    self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
                    return data

            if self.heap[left_idx] <= self.heap[right_idx]:
                self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
                idx = left_idx
            else:
                self.heap[idx], self.heap[right_idx] = self.heap[right_idx], self.heap[idx]
                idx = right_idx
            
        return data
    
    def length(self):
        return len(self.heap)
    def pri(self):
        return self.heap

heap = Heap()

for __ in range(n):
    command = int(input())

    if command == 0 and heap.length() == 1:
        print(0)
    elif command == 0:
        print(heap.pop())
    else:
        heap.insert(command)
