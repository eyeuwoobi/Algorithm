import sys
from collections import deque

k = int(sys.stdin.readline())

nums = deque([])

for _ in range(k):
    now = int(sys.stdin.readline())
    if now == 0:
        nums.pop()
    else:
        nums.append(now)

print(sum(nums))