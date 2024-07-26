import sys

n = int(sys.stdin.readline())

def PS_checker(sentence):
    counter = 0
    for i in range(len(sentence)):
        if sentence[i] == '(':
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            return 'NO'
    if counter == 0:
        return 'YES'
    else:
        return 'NO'

for _ in range(n):
    string = sys.stdin.readline().rstrip()
    counter = 0
    print(PS_checker(string))