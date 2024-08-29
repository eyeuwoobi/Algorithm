import sys

input = sys.stdin.readline

class Heap:
    
    # 클래스 초기화
    def __init__(self):
        self.heap = []
        self.heap.append(None)
    
    def check_swap_up(self, idx):
        if idx <= 1:
            return False
        parent_idx = idx // 2 
        if self.heap[parent_idx] < self.heap[idx]:
            return True
        else:
            False
    
    def insert(self, data):
        self.heap.append(data)
        idx = len(self.heap) - 1

        while self.check_swap_up(idx):
            parent_idx = idx // 2
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            idx = parent_idx
        
        return True
    
    def check_swap_down(self, idx):
        left_idx = idx * 2
        right_idx = idx * 2 + 1
        global l_flag, r_flag

        l_flag = 0
        r_flag = 0

        if len(self.heap) <= left_idx:
            return False
        elif len(self.heap) <= right_idx:
            if self.heap[idx] < self.heap[left_idx]:
                l_flag = 1
                return True
            else:
                return False
        else:
            if max(self.heap[right_idx], self.heap[left_idx]) > self.heap[idx]:
                if self.heap[left_idx] >= self.heap[right_idx]:
                    l_flag = 1
                    return True
                else:
                    r_flag = 1
                    return True
            else:
                return False
    
    def pop(self):
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        data = self.heap.pop()

        idx = 1
        while self.check_swap_down(idx):
            left_idx = idx * 2
            right_idx = idx * 2 + 1

            # if len(self.heap) <= right_idx:
            #     if self.heap[left_idx] > self.heap[idx]:
            #         self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
            #         return data
            # else:
            #     if self.heap[left_idx] >= self.heap[right_idx]:
            #         self.heap[left_idx], self.heap[idx] = self.heap[idx], self.heap[left_idx]
            #         idx = left_idx
            #     else:
            #         self.heap[right_idx], self.heap[idx] = self.heap[idx], self.heap[right_idx]
            #         idx = right_idx

            if l_flag == 1:
                if len(self.heap) <= right_idx:
                    self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
                    return data
                else:
                    self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
                    idx = left_idx
            elif r_flag == 1:
                    self.heap[idx], self.heap[right_idx] = self.heap[right_idx], self.heap[idx]
                    idx = right_idx                
                
        return data
    
    def length(self):
        return len(self.heap) - 1

n = int(input())
max_heap = Heap()

for __ in range(n):
    command = int(input())
    if command == 0 and max_heap.length() == 0:
        print(0)
    elif command == 0:
        print(max_heap.pop())
    else:
        max_heap.insert(command)