import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

max = nums[0]
min = nums[0]


for i in range(1, N):
    if max < nums[i]:
        max = nums[i]
    elif min > nums[i]:
        min = nums[i]

print(min, max)