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
    popped_nums.append(str(nums.pop(curr_idx)))
    if len(nums) == 0:
        break
    nums = nums[curr_idx:] + nums[:curr_idx]
    if k < len(nums):
        curr_idx = k % len(nums) - 1
    else:
        curr_idx = (k-1) % len(nums)
    
print('<'+', '.join(popped_nums)+'>')