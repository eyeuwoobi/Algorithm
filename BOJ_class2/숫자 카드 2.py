import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()


m = int(sys.stdin.readline())
counts = [0] * m
targets = list(map(int, sys.stdin.readline().split()))

d = {}

for i in targets:
    d[i] = int(0)

for i in nums:
    if i in d:
        d[i] += 1

for i in targets: print(d[i], end=' ')


# 이진탐색 이용 알고리즘... -> 시간복잡도로 폐기
# def bin_search(list, number):
#     pl = 0
#     pr = n - 1
#     pc = n // 2
#     while pl <= pr:
#         pc = (pl + pr) // 2
#         if list[pc] == number:
#             return pc
#         elif list[pc] > number:
#             pr = pc - 1
#         else:
#             pl = pc + 1
#     return -1

# def broad_search(list, idx, number):
#     pl = idx 
#     pr = idx
#     counter = 1
#     while True:
#         if pl > 0:
#             pl -= 1
#             if list[pl] == list[idx]:
#                 counter += 1
#             else:
#                 pl = 0
#         if pr < len(list) - 1:
#             pr += 1
#             if list[pr] == list[idx]:
#                 counter += 1
#             else:
#                 pr = len(list) - 1

#         if pl == 0 and pr == len(list) - 1:
#             return counter


# def bin_updated_right(list, idx):
#     pr = n - 1
#     pl = idx + 1
#     right_end = idx
#     while pl <= pr:
#         pc = (pl + pr) // 2
#         if list[pc] == list[idx]:
#             if right_end < pc: 
#                 right_end = pc
#                 pl = right_end + 1
#             else:
#                 return right_end
#         elif list[pc] > list[idx]:
#             pr = pc - 1
#         else:
#             pl = pc + 1
#         if right_end == pr: return right_end
#     return -1  

# def bin_updated_left(list, idx):
#     if idx == 0: pr = 0
#     else: pr = idx - 1
#     pl = 0
#     left_end = idx
#     while pl <= pr:
#         pc = (pl + pr) // 2
#         if list[pc] == list[idx]:
#             if left_end > pc: 
#                 left_end = pc
#                 pr = left_end - 1
#             else:
#                 return left_end
#         elif list[pc] > list[idx]:
#             pr = pc - 1
#         else:
#             pl = pc + 1
#         if left_end == pl:
#             return left_end
#     return -1  
        

# for i in range(len(targets)):
#     idx = bin_search(nums, targets[i])
#     if idx == -1:
#         pass
#     else:
#         counts[i] = (bin_updated_right(nums, idx) - bin_updated_left(nums, idx)) + 1

print(*counts, sep=' ')
