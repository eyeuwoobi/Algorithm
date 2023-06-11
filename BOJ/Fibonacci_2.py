n = int(input())

nums = [0, 1, 1]


while len(nums) <= n:
    fibonacci = nums[-1] + nums[-2]
    nums.append(fibonacci)

print(nums[-1])
