import random

board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

ship = [[0, 0], [0, 1], [0, 3], [0, 4]]
long = 4

def random_ship():
    global ship
    x = random.randint(0, 8)
    y = random.randint(0, 8)
    d =  random.randint(0, 1)
    if d == 0:
        if d == 0:
            ship = [[x, y], [x, y + 1], [x, y + 2], [x, y + 3]]
        else:
            ship = [[x, y], [x + 1, y], [x + 2, y], [x + 3, y]]

def show_board():
    for row in board:
        print('|'. join(row))
        print('-'* 15)

def where_attack():
    global long
    print('Укажите строку:')
    strocka = int(input())
    print('Укажите ряд:')
    ryad = int(input())

    if [strocka, ryad] in ship:
        if [strocka, ryad] != '#':
            print('Hit')
        board[strocka][ryad] = '#'
        long = long - 1
        if long == 0:
            print('Утонул')

    else:
        print('Miss')
        board[strocka][ryad] = '*'

show_board()
random_ship()
for i in range(10):
    where_attack()
    show_board()
