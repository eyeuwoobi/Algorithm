import sys

nums = []

while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break

sorted_nums = sorted(nums)
max = sorted_nums[-1]
idx = nums.index(max) + 1

print(max)
print(idx)