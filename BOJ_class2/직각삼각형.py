import sys

while True:
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    a, b, c = nums
    if c == 0:
        break

    if c**2 == a**2 + b**2:
        print('right')
    else:
        print('wrong')