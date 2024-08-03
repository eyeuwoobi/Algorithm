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

def bin_Search(list, length):
    nl = 1
    nr = length
    while nr - nl > 1:
        counter = 0
        nc = (nl + nr) // 2
        for s in sticks:
            counter += s // nc
        if counter >= n:
            nl = nc 
        else: 
            nr = nc 
    count_left = 0
    count_right = 0
    for s in sticks:
        count_left += s // nl
        count_right += s // nr
    if count_right >= n:
        return nr
    else:
        return nl

# for i in range(ideal_length):
#     reduced_sticks = [s // (ideal_length - i) for s in sticks]
#     if sum(reduced_sticks) >= n:
#         print(ideal_length - i)
#         break

print(bin_Search(sticks, ideal_length))
