import sys

N = int(sys.stdin.readline())

level = 0
summation = 1
while True:
    summation += 6 * level
    if N <= summation:
        print(level + 1)
        break
    level += 1
