import sys

first = list(map(int, sys.stdin.readline().split()))
second = list(map(int, sys.stdin.readline().split()))

if first[0] > second[0]:
    min_x = second[0]
else:
    min_x = first[0]

if first[1] > second[1]:
    min_y = second[1]
else:
    min_y = first[1]

if first[2] > second[2]:
    max_x = first[2]
else:
    max_x = second[2]

if first[3] > second[3]:
    max_y = first[3]
else:
    max_y = second[3]

if max_x - min_x > max_y - min_y:
    sq = max_x - min_x
else:
    sq = max_y - min_y

area = sq ** 2
print(area)