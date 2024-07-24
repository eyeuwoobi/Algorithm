import sys

n = int(sys.stdin.readline())
nums = []


if n <= 4:
    for i in range(n):
        nums.append(i+1)


    for i in range(n):
        if i == n-1:
            print(nums[0])
            break
        else:
            nums.pop(0)
            nums.append(nums[0])
            nums = nums[1:]

else:
    print((n-4)*2)