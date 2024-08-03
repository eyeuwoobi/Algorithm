import sys

intput = sys.stdin.readline

n = int(input())
nums = []
commands = []
my_nums = [i for i in range(1, n+1)]
my_stack = [0]
break_counter = 0

for _ in range(n):
    nums.append(int(input()))

for i in range(n):
    while nums[i] > my_stack[-1]:
        commands.append('+')
        my_stack.append(my_nums.pop(0))
    if nums[i] == my_stack[-1]:
        commands.append('-')
        my_stack.pop()
    if nums[i] < my_stack[-1]:
        print('NO')
        break_counter += 1
        break

if break_counter == 0:
    print(*commands, sep='\n')