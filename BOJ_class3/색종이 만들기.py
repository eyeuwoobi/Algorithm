import sys

input = sys.stdin.readline

n = int(input())
graph = []


#그래프 입력받기 그리디?
for __ in range(n):
    graph.append(list(map(int, input().split())))

mesh_size = n

blue_origami = 0
blue_sum = 0
white_origami = 0
white_sum = 0


while blue_sum + white_sum != n ** 2:
    start_point_x = 0
    start_point_y = 0
    while start_point_y + mesh_size < n:
        while start_point_x + mesh_size < n:
            sum()

