# Напишите программу, которая получает длины двух катетов в прямоугольном треугольнике и выводит его
# площадь. Каждое число записано в отдельной строке.


# num1 = int(input("Enter the 1 number "))
# num2 = int(input("Enter the 2 number "))
# s = ((num1*num2)/2)
# print(s)


# В школе решили набрать три новых математических класса. Так как занятия по математике у них
# проходят в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты.
# За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов.
# Сколько всего нужно закупить парт чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа:
# количество учащихся в каждом из трех классов.

# num1 = int(input("Enter the 1 number "))
# num2 = int(input("Enter the 2 number "))
# num3 = int(input("Enter the 3 number "))
# print(f"(1 grade + 2 grade + 3 grade) //2 == desks  {(num1 + num2 + num3) // 2 }")


# Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают),
# 2 (если два совпадает) или 0 (если все числа различны).


# num1 = int(input("Enter the 1 number "))
# num2 = int(input("Enter the 2 number "))
# num3 = int(input("Enter the 3 number "))
# if num1 == num2 and num2 == num3:
#     print("3")
# elif num1 == num2 or num2 == num3 or num3 == num1:
#     print("2")
# else:
#     print("0")

# Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO. Напомним,
# что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4,
# но не кратен 100, а также если он кратен 400.


# num1 = int(input("Enter the year please "))
# if num1 %4 == 0 and num1 %100 !=100 or num1 %400 == 0:
#     print("YES")
# else:
#     print("NO")

# Камень ножницы бумага
# Rock Paper Scossors
game = True
while game
    #Variables
    player1_score = 0
    player2_score = 0
    player1_choice = ''
    player2_choice = ''
    rounds = 3
    #Start of game
    for i in range(1,rounds+1):
        #Enter data
        player1_choice = str(input("Enter your choice player 1: [r],[p],[s] : "))#r
        player2_choice = str(input("Enter your choice player 2: [r],[p],[s] : "))#p
        #Compare data
        # if player1_choice == 'r':
        #     if player2_choice == 's':
        #         print('Player 1 win the round!')
        #         player1_score = player1_score + 1
        #     elif player2_choice == 'p':
        #         print('Player 2 win the round!')
        #         player2_score = player2_score + 1
        #     else:
        #         print('Draw round')
        if player1_choice == player2_choice:
            print('Draw round')
        elif player1_choice == 'r':
            if player2_choice == 's':
                print('Player 1 win the round!')
                player1_score = player1_score + 1
            else:
                print('Player 2 win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 'p':
            if player2_choice == 'r':
                print('Player 1 win the round!')
                player1_score = player1_score + 1
            else:
                print('Player 2 win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 's':
            if player2_choice == 'p':
                print('Player 1 win the round!')
                player1_score = player1_score + 1
            else:
                print('Player 2 win the round!')
                player2_score = player2_score + 1
    #Compare score
    if player1_score > player2_score:
        print('Player 1 win the game!')
    elif player2_score > player1_score:
        print('Player 2 win the game!')
    else:
        print('Draw game!')
game = bool(input("If you want contimue press any key : "))