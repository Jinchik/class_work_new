# gender =  'male'#female
# age = 13
# if gender == 'male':
#     if age < 18:
#         print('You are a boy')
#     else:
#         print('You are a man')
# elif gender == 'female':
#     if age < 18:
#         print('You are a girl')
#     else:
#         print('You are a woman')
# else:
#     if age <18:
#         print('A child')
#     else:
#         print('An adult')

# calc
# numb1=int(input('Enter your first number '))
# numb2 =int(input('Enter your second number '))
# oper =int(input('Enter your operator '))
# if oper == '+':
#     print(numb + numb2)


# calc2 Мой вариант

# numb1 = "t"
# numb2 = 2
# command = '+'
# if type(numb1) == type(1):
#     if type(numb2) == type(1):
#
#         if command == '+':
#             print(numb1, command, numb2, '=', numb1 + numb2)
#         elif command == '-':
#             print(numb1, command, numb2, '=', numb1 - numb2)
#         elif command == '*':
#             print(numb1, command, numb2, '=', numb1 * numb2)
#         elif command == '/':
#             if numb1 != 0:
#                 print(numb1, command, numb2, '=', numb1 / numb2)
#             else:
#                 print('Zero division')
#         else:
#             print('Incorrect command')
#     else:
#         print('Number2 is not integer')
# else:
#     print('Number1 is not integer')




# # Ctrl +Alt +L = PEP 8, выделить все и tab = отступ вправо на 4 пробела, shift + tab влево на 4.







number1 = input("Enter number1 : ")
command = input("Enter command : ")
number2 = input("Enter number2 : ")
if type(number1) == type(1):
    if type(number2) == type(1):
        number1 = int(number1)
        number2 = int(number2)
        if command == '+':
            print(number1, command, number2, '=', number1 + number2)
        elif command == '-':
            print(number1, command, number2, '=', number1 - number2)
        elif command == '*':
            print(number1, command, number2, '=', number1 * number2)
        elif command == '/':
            if number2 != 0:
                print(number1, command, number2, '=', number1 / number2)  # PEP 8 Ctrl + Alt + L
            else:
                print('Zero division')
        else:
            print('Incorrect command')
    else:
        print('Number2 is not int')
else:
    print('Number1 is not int')