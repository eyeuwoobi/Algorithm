import sys
import math

while True:
    string = sys.stdin.readline().rstrip()
    designator = 0
    if string == '0':
        break
    if len(string) == 1:
        print('yes')
        continue
    else:
        for i in range(math.floor(len(string) / 2)):
            if string[i] == string[-(i+1)]:
                pass
            else:
                print('no')
                designator = 1
                break
    if designator == 0 and len(string) > 1:
        print('yes')