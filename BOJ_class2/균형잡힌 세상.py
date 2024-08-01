import sys

while True:
    string = input()
    if string == '.':
        break
    removed_string = string.replace(' ', '')
    break_counter = 0
    stack = []
    for i in range(len(removed_string)):
        if removed_string[i] == '(' or removed_string[i] == '[':
            stack.append(removed_string[i])
        elif removed_string[i] == ')':
            if len(stack) == 0:
                print('no')
                break_counter += 1
                break
            elif stack[-1] == '(' :
                stack.pop()
            else:
                print('no')
                break_counter += 1
                break
        elif removed_string[i] == ']':
            if len(stack) == 0:
                print('no')
                break_counter += 1
                break
            elif stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break_counter += 1
                break
    if len(stack) > 0 and break_counter == 0:
        print('no')
        break_counter += 1
    if break_counter == 0:
        print('yes')    
    