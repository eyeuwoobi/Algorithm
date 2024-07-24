import sys

available_meal = list(map(int, sys.stdin.readline().split()))
requested_meal = list(map(int, sys.stdin.readline().split()))

not_meal = 0

for i in range(len(available_meal)):
    if requested_meal[i] - available_meal[i] > 0:
        not_meal += requested_meal[i] - available_meal[i]

print(not_meal)