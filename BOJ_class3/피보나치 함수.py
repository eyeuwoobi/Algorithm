import sys

input = sys.stdin.readline

t = int(input())

# def fibonacci(list, n):
#     if n == 0:
#         list[0] += 1
#     elif n == 1:
#         list[1] += 1
#     else:
#         return fibonacci(list, n-1) + fibonacci(list, n-2)

for _ in range(t):
    n = int(input())
    zeros = [1, 0]
    ones = [0, 1]
    if n <= 1:
        print(zeros[n], end=' ')
        print(ones[n])
    else:
        while n > 1:
            zeros.append(zeros[-1] + zeros[-2])
            ones.append(ones[-1] + ones[-2])
            n -= 1
        print(zeros[-1], end=' ')
        print(ones[-1])