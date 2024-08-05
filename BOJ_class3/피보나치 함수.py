import sys

input = sys.stdin.readline

t = int(input())

def fibonacci(list, n):
    if n == 0:
        list[0] += 1
        return 0
    elif n == 1:
        list[1] += 1
        return 1
    else:
        return fibonacci(list, n-1) + fibonacci(list, n-2)

for _ in range(t):
    counter = [0] * 2
    fibonacci(counter, int(input()))
    print(*counter, sep=' ')