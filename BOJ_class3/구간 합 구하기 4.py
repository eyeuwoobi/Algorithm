import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
nums = [0] + list(map(int, input().rstrip().split()))
for _ in range(m):
    dp = []
    i, j = map(int, input().rstrip().split())
    