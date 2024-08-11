import sys

input = sys.stdin.readline

n, m = map(int, input().split())
name_dict = dict()
num_dict = dict()

for i in range(n):
    name = input().rstrip()
    name_dict[name] = i + 1
    num_dict[i+1] = name

for _ in range(m):
    quiz = input().rstrip()
    try:
        number = int(quiz)
        print(num_dict[number])
    except ValueError:
        print(name_dict[quiz])
    