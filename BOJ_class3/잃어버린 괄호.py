import sys
import re

input = sys.stdin.readline

expression = str(input().rstrip())

listed_formula = re.split(r'([+|-])', expression)

for i in range(len(listed_formula)):
    try:
        number = int(listed_formula[i])
        listed_formula[i] = number
    except:
        pass

listed_formula = ['+'] + listed_formula

result = 0

if listed_formula.count('+') == 1 or listed_formula.count('-') == 0:
    for i in listed_formula:
        try:
            number = int(i)
            if operand == '+':
                result += number
            else:
                result -= number
        except:
            operand = i

else:
    sign = 0
    minus = 0
    for i in listed_formula:
        try:
            number = int(i)
            if operand == '+' and sign == 0:
                result += number
            if operand == '+' and sign != 0:
                minus += number
            if operand == '-':
                result -= minus
                minus = 0
                minus += number
        except:
            operand = i
            if operand == '-':
                sign += 1
    result -= minus

print(result)
