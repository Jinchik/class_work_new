# #Объявление функции
# def hello():
#     print('Hello world')
# #Вызов функции
# hello()
# hello()
# hello()
# hello()
# hello()
# def hello_name(name): #аргументы, атрибуты функции, переменные функции, #Параметры функции
#     #Тело функции
#     print(f"Hello{name}")
# hello_name(' Alex')
# hello_name(' George')
# hello_name(' Kate')


# Задание 1
# Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't let the noise of others' opinions
# drown out your own inner voice.”
# Steve Jobs


# def ste():
#     print(f"“Don't let the noise of others\' opinions\n drown out your own inner voice.”\n Steve Jobs")
# ste()
# def steve():
#     print(f"“Don\'t let the noise of others\' opinions \ndrown out your own inner voice.” \n\t\t\t\t\t\t\t\tSteve Jobs")
# steve()


# Задание 2
# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все нечетные числа
# между ними.


# def odd(a,b): #Параметры функции
#     for i in range(a, b + 1):
#         if i % 2 != 0:
#             print(i)
# number1 = int(input("Num 1 "))
# number2 = int(input("Num 2 "))
#
# odd(number1,number2)


# Задание 4
# Напишите функцию, которая возвращает максимальное из четырёх чисел. Числа передаются в качестве
# параметров.
#
# def ma(a,b,c,d):
#     max = 0
#     if a>b:
#         max = a
#     elif b>c:
#         max = b
#     elif c>d:
#         max = c
#     elif d>a:
#         max = d
#     print(max)
# ma(1,15,9,10)

# def maxi(a,b,c,d):
#     if a >= b and a >= c and a >= d:
#         print(a)
#     if b >= a and b >= c and b >= d:
#         print(b)
#     if c >= a and c >= b and c >= d:
#         print(c)
#     if d >= a and d >= b and d >= c:
#         print(d)
# maxi(1,2,3,4)


# Задание 3
# Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
# Функция принимает в качестве параметра: длину линии,
# направление, символ.
#
# def line(length, direction, symbol):
#     s = ''
#     while length > 0:
#
#         if direction == 'horizontal':
#             s = s + symbol
#         elif direction == 'vertical':
#             s = s + '\n' + symbol
#         length = length - 1
#     return s
# a = line(5,'vertical','%')
# print(a)
# Функциональный подход
# Функция выполняет 1 функцию за раз
# Изолирована Вход>Работа>Выход


# '''Задание 5
# Напишите функцию, которая возвращает сумму чисел
# в указанном диапазоне. Границы диапазона передаются
# в качестве параметров.'''

# def sum(a, b):
#     sm = 0
#     if a >= b:
#         a, b = b, a
#     for i in range(a, b):
#         sm = sm + i
#     return sm
#
#
# a = sum(122, 11120)
# print(a)

# def square(a,b,c):
#     sapace = " "
#     for i in range(a):
#         if i == 0 or i == (a - 1):
#             print(b * c)
#         else:
#             print(c + ((b - 2) * sapace) + c)
# square(5,5,"*")



# Задание 6
# Напишите функцию, которая проверяет является ли
# число простым. Число передаётся в качестве параметра.
# Если число простое нужно вернуть из метода true, иначе
# false.
def simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True