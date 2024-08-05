import sys

input = sys.stdin.readline

n = int(input())

times = list(map(int,input().split()))

times.sort()

summation = 0
for i in range(n):
    summation += times[i] * (n - i)

print(summation)