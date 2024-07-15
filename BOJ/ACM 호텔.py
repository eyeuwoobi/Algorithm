import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    if N % H == 0:
        room = str(N // H)
        floor = str(H)
    else:
        room = str(N // H + 1)
        floor = str(N % H)
    if len(room) == 1:
        room = '0' + room
    print(floor + room)