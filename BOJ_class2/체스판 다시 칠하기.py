import sys

n, m = map(int, sys.stdin.readline().split())
org_board = []
for _ in range(n):
    org_board.append(sys.stdin.readline().rstrip())

def w_board_maker(n, m):
    list = []
    for i in range(n):
        raw = ''
        if i % 2 == 0:
            for j in range(m):
                if j % 2 == 0:
                    raw += 'W'
                else:
                    raw += 'B'
        else:
            for j in range(m):
                if j % 2 == 0:
                    raw += 'B'
                else:
                    raw += 'W'
        list.append(raw)
    return list

def b_board_maker(n, m):
    list = []
    for i in range(n):
        raw = ''
        if i % 2 == 0:
            for j in range(m):
                if j % 2 == 0:
                    raw += 'B'
                else:
                    raw += 'W'
        else:
            for j in range(m):
                if j % 2 == 0:
                    raw += 'W'
                else:
                    raw += 'B'
        list.append(raw)
    return list

w_chess_board = w_board_maker(n, m)
b_chess_board = b_board_maker(n, m)

def checker_maker(n, m):
    list = []
    for i in range(n):
        list.append([0] * m)
    return list

w_checker = checker_maker(n, m)
b_checker = checker_maker(n, m)

def checker(org_board, board, signal):
    if signal == 'w':
        checker = w_checker
    else:
        checker = b_checker
    for raw in range(n):
        for i in range(m):
            if org_board[raw][i] == board[raw][i]:
                pass
            else:
                checker[raw][i] = 1
    return checker
  
w_counter = checker(org_board, w_chess_board, signal='w')
b_counter = checker(org_board, b_chess_board, signal='b')

reduced_raws = n - 8
reduced_columns = m - 8

def painting_machine(counter):
    min_counter = n * m
    for raw in range(reduced_raws+1):
        for column in range(reduced_columns+1):
            painting_counter = 0
            for i in range(8):
                painting_counter += sum(counter[raw+i][column:column+8])
            if min_counter > painting_counter:
                min_counter = painting_counter
    return min_counter

min_w = painting_machine(w_counter)
min_b = painting_machine(b_counter)

print(min(min_b, min_w))