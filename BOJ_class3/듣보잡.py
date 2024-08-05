import sys

input = sys.stdin.readline

n, m = map(int, input().split())

d = set()
b = set()

for _ in range(n):
    d.add(input().rstrip())

for _ in range(m):
    b.add(input().rstrip())

b_d = b & d
my_list = list(b_d)
my_list.sort()

print(len(my_list))
print(*my_list, sep='\n')