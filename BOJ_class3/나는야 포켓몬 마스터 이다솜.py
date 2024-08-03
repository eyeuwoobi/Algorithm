import sys

input = sys.stdin.readline

n, m = map(int, input().split())
d = dict()
ps = []

# for i in range(n):
#     name = input().rstrip()
#     d[name] = str(i+1)
    
# # for _ in range(m):
# #     quiz = input().rstrip()
# #     if quiz in d:
# #         print(d[quiz])
# #     else:
# #         for k, v in d.items():
# #             if v == quiz:
# #                 print(v)

for _ in range(n):
    ps.append(input().rstrip())

for _ in range(m):
    quiz = input().rstrip()
    