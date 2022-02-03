# list = []
# tuple = (,) - хотя бы 2 элемента разделенных запятой
# dict = {}


# tuple / dict
# tuple кортеж (массив)
# итерируемый тип данных\ не изменяемый тип данных \ индексируемый
# не изменяемый список
# bucket = ('Tomato', 'Bread', 'Butter')
# # a = 2
# # b = 3
# # a,b = b,a
# # print(a,b)
# a = [1]
# b = [2]
# c = [3]
# trio = (a, b, c)
# print(trio)
# a[0] = 10
# b[0] = 22
# c[0] = 0
# print(trio)



#dict словарь(массив)
# итерируемый тип данных\ не изменяемый тип данных \ ключ значения\ неупорядоченный тип данных
countries = {'Ukrain':'Kyiv', 'Poland':'Warshava'}
d = {0:'Andrey', 'a': 'Forever', 'k':3}
#ключ - любой неизменяемый тип данных : значение - любой тип данных
print(d)
print(d['a'])
d['a'] = ['Never', 'Forever']
print(d)
print(d['a'][0])
d['b'] = 'abc' #Add new element
print(d)
d.pop('k')  #delte by key and pop it
print(d)
#d.popitem('Andrey')  # delete by key, value
print(d.keys())
print(d.values())