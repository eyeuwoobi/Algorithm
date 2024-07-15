import sys

scale = list(map(int, sys.stdin.readline().split()))

ass_sorted_scale = sorted(scale)
des_sorted_scale = sorted(scale, reverse=True)

if ass_sorted_scale == scale:
    print('ascending')
elif des_sorted_scale == scale:
    print('descending')
else:
    print('mixed')