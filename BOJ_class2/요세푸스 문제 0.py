import sys

n, k = map(int, sys.stdin.readline().split())

t = 1
nums = []
popped_nums = []
while t <= n:
    nums.append(t)
    t += 1

curr_idx = k - 1

for i in range(n):
    popped_nums.append(nums.pop(curr_idx))
    if len(nums) == 0:
        break
    curr_idx = (curr_idx + k) % len(nums)
    
print(nums)
print(*popped_nums)