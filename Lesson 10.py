# a = 1
# b = 10
# while a <= b and a != 5:
#     print(a)
#     a = a + 1
#
#
# a = 1
# b = 10
# for i in range(a,b+1):
#     if i == 5:
#         break
#     print(i)


# a=1
# b=10
# while True:
#     print(a)
#     a= a+1
#     if a == 5:
#         break


# a = 1
# b = 10
# for i in range(a,b+1):
#     if i ==5:
#         continue
#     print(i)


# Задание 3
# Пользователь вводит с клавиатуры две границы диапазона и число. Если число не попадает в диапазон,
# программа просит пользователя повторно ввести число,
# и так до тех пор, пока он не введет число правильно. Программа отображает все числа диапазона, выделяя число
# восклицательными знаками. Например:
# 1 2 3 !4! 5 6 7.


# a = 1
# b = 10
# guess = 4
# if a <= guess and guess <=b:
#     for i in range(a,b+1):
#         if i == guess:
#             print('!',i,'!', sep='', end = ' ')
#         else:
#             print(i, end = ' ')


# Задание 1
# Пользователь вводит с клавиатуры размер стороны
# квадрата. Требуется отобразить на экран заполненный
# квадрат. Размер стороны равен введённому размеру.
# Например, если пользователь ввёл 3 на экране будет
# выведено:
# ***
# ***
# ***


# a = int(input("Enter a height "))
# b = int(input("Enter a weight "))
# c = str(input("Enter a symbol "))
# for i in range (a):
#     print(b*c)


# Задание 3
# Пользователь вводит с клавиатуры размер стороны
# квадрата. Требуется отобразить на экран незаполненный квадрат (отображаются только границы квадрата).
# Размер стороны равен введённому размеру.


# Задание 2
# Пользователь вводит с клавиатуры ширину и высоту прямоугольника. Требуется отобразить на экран
# заполненный прямоугольник с указанными высотой и
# шириной. Например, если пользователь ввёл высоту 3,
# а ширину 5 на экране будет выведено:
# *****
# *****
# *****


# a = 5
# b = 5
# c = "*"
# sapace = " "
# for i in range(a):
#     if i == 0 or i == (a - 1):
#         print(b * c)
#     else:
#         print(c + ((b - 2) * sapace) + c)
