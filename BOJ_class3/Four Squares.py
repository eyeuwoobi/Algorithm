import sys

input = sys.stdin.readline

def checker(n):
    if n == 7:
        return 4
    squares = set([i**2 for i in range(1, 224)])
    if n in squares:
        return 1
    for square in squares:
        if n - square in squares:
            return 2
    while n % 4 == 0:
        n //= 4
    if (n - 7) % 8 == 0:
        return 4
    return 3 


n = int(input())
print(checker(n))