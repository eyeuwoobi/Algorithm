import sys
k, n = map(int, sys.stdin.readline().split())

sticks = []
hap = 0

for _ in range(k):
    stick = int(sys.stdin.readline())
    hap += stick
    sticks.append(stick)
max_stick = max(sticks)
ideal_length = hap // n

for i in range(ideal_length):
    reduced_sticks = [s // (ideal_length - i) for s in sticks]
    if sum(reduced_sticks) >= n:
        print(ideal_length - i)
        break