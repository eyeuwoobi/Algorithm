import sys

input = sys.stdin.readline

n, k = map(int, input().split())

types = []
for _ in range(n):
    types.append(int(input()))

types.reverse()

counter = 0

for coin in types:
    counter += k // coin
    k -= (k // coin) * coin

print(counter)