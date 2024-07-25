import sys
from collections import deque

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(i+1)

queue = deque(nums)

while len(queue) > 1:
    queue.popleft()
    a = queue.popleft()
    queue.append(a)

print(queue.popleft())