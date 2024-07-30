import sys

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()

def up(a, b):
    return (a+b//2)//b

def mean(list, length):
    return up(sum(list), n)

def median(list, length):
    return list[length // 2]

def mode(ns):
    d = {}
    for i in ns:
        if i not in d: d[i] = int(1)
        else: d[i] += 1
    counter = list(d.values())
    counter.sort()
    max_counter = counter[-1]
    keys = [k for k, v in d.items() if v == max_counter]
    keys.sort()
    if len(keys) == 1:
        return keys[0]
    else: return keys[1]

print(mean(nums, n))
print(median(nums, n))
print(mode(nums))
print(nums[-1] - nums[0])