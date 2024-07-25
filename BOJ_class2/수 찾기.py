import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

def bin_search(list, number):
    pl = 0
    pr = n - 1
    pc = n // 2
    while pl <= pr:
        pc = (pl + pr) // 2
        if list[pc] == number:
            return 1
        elif list[pc] > number:
            pr = pc - 1
        else:
            pl = pc + 1
    return 0
        
for target in targets:
    print(bin_search(nums, target))
    