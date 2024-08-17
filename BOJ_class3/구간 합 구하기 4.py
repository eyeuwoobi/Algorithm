import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
nums = [0] + list(map(int, input().rstrip().split()))
a = 0
dp = []
for i in nums:
    a += i
    dp.append(a)

for _ in range(m):
    i, j = map(int, input().rstrip().split())
    print(dp[j]-dp[i-1])