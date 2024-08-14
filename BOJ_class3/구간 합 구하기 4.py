import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
nums = [0] + list(map(int, input().rstrip().split()))
r_max = 1
l_min = n
for _ in range(m):
    dp = []
    i, j = map(int, input().rstrip().split())
    