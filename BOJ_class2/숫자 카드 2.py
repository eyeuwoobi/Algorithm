import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()


m = int(sys.stdin.readline())
counts = [0] * m
targets = list(map(int, sys.stdin.readline().split()))

def bin_search(list, number):
    pl = 0
    pr = n - 1
    pc = n // 2
    while pl <= pr:
        pc = (pl + pr) // 2
        if list[pc] == number:
            return pc
        elif list[pc] > number:
            pr = pc - 1
        else:
            pl = pc + 1
    return -1

def broad_search(list, idx, number):
    pl = idx 
    pr = idx
    counter = 1
    while True:
        if pl > 0:
            pl -= 1
            if list[pl] == list[idx]:
                counter += 1
            else:
                pl = 0
        if pr < len(list) - 1:
            pr += 1
            if list[pr] == list[idx]:
                counter += 1
            else:
                pr = len(list) - 1

        if pl == 0 and pr == len(list) - 1:
            return counter


for i in range(len(targets)):
    idx = bin_search(nums, targets[i])
    if idx == -1:
        pass
    else:
        counts[i] = broad_search(nums, idx, targets[i])

print(*counts, sep=' ')