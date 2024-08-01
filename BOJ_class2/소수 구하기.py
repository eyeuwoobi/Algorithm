import sys
import math

m, n = map(int, sys.stdin.readline().split())

nums = [i for i in range(m, n+1)]

for number in nums:
    division = 0
    if number == 1:
        continue
    for divider in range(2, math.floor(math.sqrt(number))+1):
        if number % divider == 0:
            division += 1
            break
    if division == 0:
        print(number)
