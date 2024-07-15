import sys

S = str(sys.stdin.readline().rstrip())
outcome = []

for i in range(97, 123):
    outcome.append(S.find(chr(i)))

print(*outcome, sep=' ')