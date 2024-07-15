import sys

T = int(sys.stdin.readline())

for _ in range(T):
    results = sys.stdin.readline().rstrip()
    streak = 0
    sum = 0
    for i in range(len(results)):
        if results[i] == 'O':
            score = streak + 1
            streak += 1
        if results[i] == 'X':
            score = 0
            streak = 0
        sum += score
    print(sum)
        