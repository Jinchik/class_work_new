# STR методы строк
# Итерируемы тип данных\не изменяемый тип данных\ индексируемый
# h = 'Hello World'
# print(h)
# print(h[0])
# h = h + '?'
# print(h)
# print(h[0])
# print(h[1])
# print(h[2])
# print(h[2])
# print(h[7])

# n = 'Alex Cherniak'
# print(n[5],n[6],n[7],n[7],n[8])
# print(n[8],n[0],n[10],n[9])
# print(n[8],n[0],n[8],n[7])

# Задание 1
# Пользователь вводит с клавиатуры строку. Произведите поворот строк и полученный результат выведите
# на экран.


# s = 'Hello World!'
# print(len(s))
# for i in range(len(s)):
#     print(s[i])
#


# s = 'Hello World!'
# rs =''
# for i in range(len(s)):
#     rs = s[i] + rs
# print(rs)


# s = 'Hello World!'
# for i in range(1,len(s)+1):
#     print(s[-i])








# '''Задание 2
# Пользователь вводит с клавиатуры строку. Посчитайте количество букв,
# цифр в строке. Выведите оба
# количества на экран.'''



#1 вариант
# letters = 'abcdefghijklmnopqrstuvxyz'
# numbers = '0123456789'
# s = 'hello123'
# count_numbers = 0
# count_letter = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     for l in range(len(letters)):
#         if a == letters[l]:
#             count_letter = count_letter + 1
#     for n in range(len(numbers)):
#         if a == numbers[n]:
#             count_numbers = count_numbers + 1
# print(count_numbers,count_letter)

# 2 вариант

# s = 'hello123'
# count_numbers = 0
# count_letters = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     if a.isalpha():
#         count_letters = count_letters + 1
#     if a.isnumeric():
#         count_numbers = count_numbers + 1
# print(count_numbers,count_letters)


# Задание 3
# Пользователь вводит с клавиатуры строку и символ
# для поиска. Посчитайте сколько раз в строке встречается
# искомый символ. Полученное число выведите на экран.

#Var 1
# s = 'Abrakadabra'
# symbol = 'a'
# count = 0
# for l in range(len(s)):
#     a = s[l]
#     if a == symbol:
#         count = count+1
# print(count)


#Var 2
# w = "Abra Kadabra"
# symb = "a"
# count = 0
# for i in w:
#         if i == symb:
#             count = count + 1
# print(count)


#var 3

s = 'Abrakadabra'
symbol = 'a'
count = 0
for l in range(len(s)):
    if s[l] == symbol:
        count = count+1
print(count)
print(s.count(symbol))