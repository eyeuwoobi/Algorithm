import sys

n = int(sys.stdin.readline())

org_levels = []

def up(a, b):
    return (a+b//2)//b

excluded_nums = up(n*3, 20)

for _ in range(n):
    org_levels.append(int(sys.stdin.readline()))
org_levels.sort()

levels = org_levels[excluded_nums:n-excluded_nums]
if len(levels) == 0:
    print('0')
else:
    print(up(sum(levels), len(levels)))