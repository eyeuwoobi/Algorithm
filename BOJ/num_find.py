#수 찾기(#1920)

from typing import Any, Sequence

N = int(input())
Ns = list(map(int, input().split()))

M = int(input())
Ms = list(map(int, input().split()))

Ns.sort()
Ms.sort()

if Ns[1] < Ms[0]:
    Ns.remove(Ns[0])

if Ns[-2] > Ms[-1]:
    Ns.remove(Ns[-1])


def bin_search(a :Sequence, key :Any) -> int:
    pl = 0
    pr = N - 1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return 1
        elif key < a[pc]:
            pr = pc - 1
        else:
            pl = pc + 1
        if pl > pr:
            break
    return 0


for i in Ms:
    if bin_search(i) == 0:
        print('0')
    else:
        print('1')