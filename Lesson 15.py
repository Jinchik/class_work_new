# List список (массив) *двусвяный список (тип хранения в памяти)
# итерируемый тип данных\ изменяемый тип данных \ индексируемый

# l = [1, 2, 3.3, True, False, 'FFF']
# l = []
# l = list()
# fruits = ['Apple', 'Pear', 'Peach', 'Mellon', 'Watermellon','Grape']
# print(fruits[0])
# print(fruits[3])
# print(fruits[-1])
# print(fruits[0:3])
# fruits[0] = 'Pineapple'
# print(fruits)
# fruits = ['Apple', 'Pear', 'Peach', 'Mellon', 'Watermellon','Grape']
# fruits[-3] = 'yellow'
# fruits[-1] = 'green'
# print(fruits)


# colors = ['Red', 'Green', 'Blue']
# print(colors)
# colors.append('Orange')

# Append to the start of the list
# colors = ['Red', 'Green', 'Blue']
# colors = colors[::-1]
# colors.append('Yellow')
# colors = colors[::-1]
# print(colors)
# colors.insert(2,'Yellow')
# print(colors)
# colors.pop(1)
# print(colors.pop(1))
# print(colors)
# colors.remove('Green')
# print(colors)
# print('Purple' in colors)
# print(len(colors))
# new_colors = colors
# print(colors)
# print(new_colors)
# colors.append('Pink')
# print(colors)
# print(new_colors)
# new_colors.append('Cyan')
# print(colors)
# print(new_colors)
# real_colors = colors[:]
# colors.pop()
# print(real_colors)
# print(colors)


# Задание 1
# В списке целых, заполненном случайными числами
# вычислить:
# ■ Сумму отрицательных чисел;
# ■ Сумму четных чисел;
# ■ Сумму нечетных чисел;
# ■ Произведение элементов с индексами кратными 3;
# ■ Произведение элементов между минимальным и
# максимальным элементом;
# ■ Сумму элементов, находящихся между первым и последним положительными элементами.


numbers = [1, 2, 3, 4, -5, 6, 5, -1, -4, 9, 20, 21, 15]
# sum_neg = 0
# sum_even = 0
# sum_odd = 0
# for number in numbers:
#     if number < 0:
#         sum_neg = sum_neg + number
#     if number % 2== 0 and number !=0:
#         sum_even = sum_even + number
#     elif number % 2 != 0 and number != 0:
#         sum_odd = sum_odd + number
# print(sum_neg,sum_odd,sum_even)
mult_3 = 1
mult_min_max = 1
minimum = numbers[0]
minimum_index = 0
maximum = numbers[0]
maximum_index = 0
for index in range(len(numbers)):
    if index % 3 == 0 and index != 0:
        mult = mult_3 * numbers[index]
    if minimum > numbers[index]:
        minimum = numbers[index]
        minimum_index = index
    if maximum < numbers[index]:
        maximum = numbers[index]
        maximum_index = index
mult_numbers = []
if maximum_index < minimum_index:
    mult_numbers = numbers[maximum_index:minimum_index]
else:
    mult_numbers = numbers[minimum_index:maximum_index]
for number in mult_numbers:
    print(mult_min_max)
    mult_min_max = mult_min_max * number
print(mult_min_max)
