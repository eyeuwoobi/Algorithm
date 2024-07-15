import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

NUM = A * B * C

string = str(NUM)
nums = []

for i in range(10):
    nums.append(string.count(f'{i}'))

for _ in nums:
    print(_)