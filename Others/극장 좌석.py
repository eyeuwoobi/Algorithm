import sys

dp = [1, 1, 2]

n = int(input())
m = int(input())

list_vip = []

for _ in range(m):
    list_vip.append(int(input()))

for i in range(3, 41):
    dp.append(dp[i-1]+dp[i-2])


methods = 1

if m == 0:
    print(dp[n])
else:
    diff = []
    diff.append(list_vip[0]-1)
    for j in range(1, m):
        diff.append(list_vip[j]-list_vip[j-1]-1)
    diff.append(n-list_vip[-1])
    for _ in diff:
        methods *= dp[_]
    print(methods)
