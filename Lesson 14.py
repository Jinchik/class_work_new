# Задание 4
# Пользователь вводит с клавиатуры строку и слово
# для поиска. Посчитайте сколько раз в строке встречается
# искомое слово. Полученное число выведите на экран. - *без использования метода count




# s = 'brobrobroheybro'
# symbol = 'bro'
# count = 0
# for l in range(len(s)):
#     a = s[l]
#     if a == symbol:
#         count = count+1
# print(count)


# s = 'Abrakadabra'
# symbol = 'ra'
# print(s.count(symbol))




# '''Задание 5
# Пользователь вводит с клавиатуры строку, слово для
# поиска, слово для замены. Произведите в строке замену
# одного слова на другое. Полученную строку отобразите
# на экране.
# * Без использования метода replace'''



# s = 'Abrakadabra'
# symbol = 'ra'
# new_symbol = 'RA'
# print(s.replace(symbol,new_symbol))
#
# print(s)




# '''Задание 1
# Есть некоторый текст. Реализуйте следующую функциональность:
# ■ Изменить текст таким образом, чтобы каждое предложение начиналось
# с большой буквы;
# ■ Посчитайте сколько раз цифры встречаются в тексте;
# ■ Посчитайте сколько раз знаки препинания встречаются в тексте;
# ■ Посчитайте количество восклицательных знаков в
# тексте.'''


#1 вариант
# t = 'some interesting, text and else. what i am doing. how do you do? i am fine! thank you.'
# symbol = ","
# print(t.count(symbol))
#
#
#
# t = 'some interesting, text and else. what i am doing. how do you do? i am fine! thank you 121212.'
# symbol =
# print(t.count(symbol))
#
#
#
#
#
# t = 'some interesting, text and else. what i am doing. how do you do? i am fine! thank you12121.'
# print(t.isalnum())


#2 вариант
# letters = 'abcdefghijklmnopqrstuvxyz'
# numbers = '0123456789'
# s1 = '!'
# s2 = ','
# t = "some interesting, text and else. what i am doing. how do you do? i am fine! thank you.12121"
# count_numbers = 0
# count_letter = 0
# count_s1 = 0
# count_s2 = 0
# for i in range(len(t)):
#     a = t[i]
#     for l in range(len(letters)):
#         if a == letters[l]:
#             count_letter = count_letter + 1
#     for n in range(len(numbers)):
#         if a == numbers[n]:
#             count_numbers = count_numbers + 1
#     for s in range(len(s1)):
#         if a == s1[s]:
#             count_s1 = count_s1 + 1
#     for ss in range(len(s2)):
#         if a == s2[ss]:
#             count_s2 = count_s2 + 1
# print(f'numbers, letters, symbol ! , symbol ,{count_numbers,count_letter,count_s1,count_s2}')


# t = 'some interesting, text and else. what i am doing. how do you do? i am fine! thank you.'
# t = t.capitalize()
# symbols = '!.?'
# for i in range(2, len(t)):
#     for s in range(len(symbols)):
#         # print(t[i - 2:i])
#         if t[i - 2:i] == (symbols[s] + ' '):
#             # print('y')
#             t = t[:i] + t[i].upper() + t[i + 1:]
# print(t)
# s = 'Hello World!'
# print(s[0:5])#Hello
# print(s[-6:-1])#World
# print(s[-6:])#World!
# print(s[:5])#Hello
# print(s[::-1])#!dlroW olleH



# word = 'Hello World!'
# for letter in word:
#     print(letter)




# number = '0123456789'
# spe = '!?,.'
# s = 'some interesting, text and else! what i am doing. how do you do? i am fine! thank you.'
# count_number = 0
# count_symbol = 0
# count_spe = 0
# count_spea = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#
#     if a in number:
#         count_number = count_number + 1
#     if a in spe:
#         count_spe = count_spe + 1
#     if a == spe[0]:
#         count_spea = count_spea + 1
# print(count_symbol, count_number, count_spe,count_spea)



word = 'Hello World!'
print(word.find('l'))
print(word.rfind('l'))
