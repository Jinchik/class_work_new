#Gues my number

# import random
# secret_number = random.randint(1,20)
# guess_number = 0
# lives = 5
# while secret_number != guess_number and lives > 0:
#     guess_number = int(input("Enter the number : "))
#     if secret_number < guess_number:
#         print('Your number greater than secret\n ')
#     elif secret_number > guess_number:
#         print('Your number lower than secret\n ')
#     lives = lives - 1
#     print(f'You have {lives} lives')
# if lives > 0:
#     print('YOU WIN')
# else:
#     print('YOU LOSE')


# Pet project



# import random
# game = True
# money = 0
# while game:
#     secret_number = random.randint(1,20)
#     guess_number = 0
#     lives = 5
#     while secret_number != guess_number and lives > 0:
#         guess_number = int(input("Enter the number : "))
#         if secret_number < guess_number:
#             print('Your number greater than secret\n ')
#         elif secret_number > guess_number:
#             print('Your number lower than secret\n ')
#         lives = lives - 1
#         print(f'You have {lives} lives')
#     if lives > 0:
#         print('YOU WIN')
#         money = money +5
#     else:
#         print('YOU LOSE')
#     print(f'YOur money {money} money')



# work = True
# while work:
#     number1 = 2#int(input("Enter number1 : "))
#     command = '+'#str(input("Enter operation : "))
#     number2 = 2#int(input("Enter number2 : "))
#     if command == '+':
#         print(f'{number1} {command} {number2} = {number1 + number2}')
#     # while command == '+':
#     #     print(f'{number1} {command} {number2} = {number1 + number2}')
#     #     command = ''
#     elif command == '-':
#         print(f'{number1} {command} {number2} = {number1 - number2}')
#     elif command == '*':
#         print(f'{number1} {command} {number2} = {number1 * number2}')
#     elif command == '/':
#         print(f'{number1} {command} {number2} = {number1 / number2}')
#     work = str(input("Press any key to continue : "))
#

#
# Задание 1
# Показать таблицу умножения для числа, введенного
# пользователем. Например, если пользователь вводит
# число 7, нужно показать:
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# num1 = 7
# num2 = 1
# while num1 > 0 and num2 <11:
#     print(f"{num1} * {num2} =  {num1 * num2}" )
#     num2 = num2+1