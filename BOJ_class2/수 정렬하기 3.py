import sys

N = int(sys.stdin.readline())

count = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(len(count)):
    counter = 1
    while counter <= count[i]:
        counter += 1
        print(i)