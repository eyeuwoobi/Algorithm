import sys
import math

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
count = 0

for number in nums:
    division = 0
    for divider in range(2, math.floor(math.sqrt(number))+1):
        if number % divider == 0:
            division += 1
            break
    if division == 0:
        count += 1

if nums.count(1) != 0:
    count -= 1

print(count)