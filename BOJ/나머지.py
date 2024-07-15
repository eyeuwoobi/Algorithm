import sys

residue = set()

for _ in range(10):
    N = int(sys.stdin.readline())
    residue.add(N % 42)

print(len(residue))