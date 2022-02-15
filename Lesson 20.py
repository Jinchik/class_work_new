# def calc(a,b):# Позиционные аргументы
#     return a+b
#
#
#
# print(calc(2,2))
#
#
# def calc(a,b, c=2): # Аргументы по умолчанию, идут после позиционных.
#     return a+b+c
#
# def calc(a,b, c=2, *args): # Неопределенное колличество позиционных аргументов
#     return a+b+c
#

# def average(*numbers):
#     count = len(numbers)
#     sum = 0
#     for number in numbers:
#         sum = sum + number
#     return sum/count
# print(average(1,2,3,4,5,6,7,8,9,0,2,4,5))

# def calc(a,b, c=2, **kwargs): # Аргументы с ключевыми словами, словарь
#     return a+b+c

# def creat_note(**notes):
#     #**notes словарь
#     return notes
# print(creat_note(lol="some1", sten='some2'))


# LEGB
# Области видемости функций
# Local(Scope) Enclosed(Scope) Global (Scope) BuiltIn

# Local
# a = 1
# b = 11
# def some():
#     a=2 # - это другая а внутри функции
#     a=a*a
#     print(a)
#     print(b)
#     print('Finish')
# print(a)  # a несуществует вне функции
# some()

# c = 2
# def local_some():
#     global c # не безопасно
#     c = c + 3
# local_some()
# print(c)


# Enclosed № nonlocal
# a = 2# В ГЛОБАЛЬНОЙ ОБЛАСТИ ВИДИМОСТИ
# def first():
#     global a
#     b = 3 # В ЛОКАЛЬНОЙ ОБЛАСТИ ВИДИМОСТИ ПО ОТНОШЕНИЮ К a
#              # В enclosed ОБЛАСТИ ВИДИМОСТИ ПО ОТНОШЕНИЮ К c
#     def second():
#         global a
#         #global b неправильно
#         nonlocal b
#         c=4 # В ЛОКАЛЬНОЙ ОБЛАСТИ ВИДИМОСТИ ПО ОТНОШЕНИЮ К a
#GLOBAL Вся ваша программа в текущем файле
#BuiltIn ОБЛАСТЬ ВИДИМОСТИ ИНТЕРПРЕТАТОРА len() del() list() str()

'''Задание 4
Написать игру «Крестики-нолики».'''
#Крестики Нолики
#Tic Tac Toe
#Variables
count = 0
player1_symbol = 'X'
player2_symbol = 'O'
player1_choice = '0'
player2_choice = '0'
board = [0,'1','2','3','4','5','6','7','8','9']
board = f'{board[1]}|{board[2]}|{board[3]}\n-----\n{board[4]}|{board[5]}|{board[6]}\n-----\n{board[7]}|{board[8]}|{board[9]}'
turn = 'X'
winner = ''
def show_board(board):
    return board
def player_choice():
    while True:
        #Game choice
        player1_choice = str(input(f'Enter your choice {player1_symbol}: '))
        #Board update
        if board[int(player1_choice)] == player1_choice:
            board[int(player1_choice)] = 'X'
            break
def check_winner():
    if board[1] == board[2] == board[3]:
        if board[1] == player1_symbol:
            winner = 'X'
            return winner
        elif board[1] == player2_symbol:
            winner = 'O'
            return winner
    if board[4] == board[5] == board[6]:
        if board[4] == player1_symbol:
            winner = 'X'
            return winner
        elif board[4] == player2_symbol:
            winner = 'O'
            return winner
    if board[7] == board[8] == board[9]:
        if board[7] == player1_symbol:
            winner = 'X'
            return winner
        elif board[7] == player2_symbol:
            winner = 'O'
            return winner
    if board[1] == board[4] == board[7]:
        if board[1] == player1_symbol:
            winner = 'X'
            return winner
        elif board[1] == player2_symbol:
            winner = 'O'
            return winner
    if board[2] == board[5] == board[8]:
        if board[2] == player1_symbol:
            winner = 'X'
            return winner
        elif board[2] == player2_symbol:
            winner = 'O'
            return winner
    if board[3] == board[6] == board[9]:
        if board[3] == player1_symbol:
            winner = 'X'
            return winner
        elif board[3] == player2_symbol:
            winner = 'O'
            return winner
    if board[7] == board[5] == board[3]:
        if board[7] == player1_symbol:
            winner = 'X'
            return winner
        elif board[7] == player2_symbol:
            winner = 'O'
            return winner
    if board[1] == board[5] == board[9]:
        if board[1] == player1_symbol:
            winner = 'X'
            return winner
        elif board[1] == player2_symbol:
            winner = 'O'
            return winner
def bot_choice():
    while True:
        #Game choice
        player2_choice = random.randint(1,9)
        if board[int(player2_choice)] == player2_choice:
            board[int(player2_choice)] = 'O'
            break

while count <= 9:
    show_board(board)
    player_choice()
    count = count + 1
    if check_winner() != '':
        break
    if count == 9:
        break
    bot_choice()
    count = count + 1

if winner == 'X':
    print('Player 1 win the game!')
elif winner == 'O':
    print('Player 2 win the game!')
elif winner == '':
    print('Draw')





#Рекурсия


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial(6))
